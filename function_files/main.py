import logging
import config as cfg
import pandas as pd
import requests
import re
from google.cloud import bigquery
import google.cloud.logging

logging_client = google.cloud.logging.Client()
logging_client.setup_logging()
logging.basicConfig(format="%(asctime)s:%(levelname)s-%(message)s", level=logging.INFO)

def authenticate_salesforce() -> dict:
    # Authenticates with Salesforce and returns the authentication response dictionary on success

    logging.info("Authenticating with Salesforce")
    response = requests.post(
        cfg.login_url,
        data={
            "client_id": cfg.client_id,
            "client_secret": cfg.client_secret,
            "grant_type": cfg.grant_type,
            "username": cfg.sf_user,
            "password": cfg.sf_pass,
        },
    )

    if response.json().get("access_token"):
        logging.info("Authentication with Salesforce succeeded")
        return response.json()
    else:
        logging.critical("Authentication with Salesfoce failed")

def pull_report(report_id, token):
    logging.info(f"Pulling report <{report_id}> from Salesforce.")

    report_url = f"{cfg.salesforce_report_url}/{report_id}?includeDetails=true"
    report = requests.get(
        report_url,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
            }
    )
    return report.json()

def pull_grouped_leadership_report(report_id, token):
    report = pull_report(report_id, token)
    if "reportMetadata" not in report:
        logging.critical(f"Could not pull {report_id}: {report[0]}")
        return

    column_names = report["reportMetadata"]["detailColumns"]
    group_column = report["reportMetadata"]["groupingsDown"][0]["name"]
    column_names.insert(0, group_column)
    column_names = [column.replace(".", "_") for column in column_names]

    groups = report["groupingsDown"]["groupings"]
    df = pd.DataFrame(columns = column_names)
    
    for group in groups:
        group_key = group['key']
        rows = []
        if report_id == "00O3m000008rKjuEAE":
            #Special case for MQL Reviewed Status Change Report
            factMapKey = f"{group_key}_0!T"
            factMapEntry = report["factMap"][factMapKey]
            rows = factMapEntry["rows"] 

        elif report_id == "00O3m000008rUViEAM":
            #Special case for Monthly Lead Movement-SQL
            second_groups = report["factMap"].keys()
            for i in second_groups:
                is_subgroup = re.search(f"^{group_key}_\d!T", i)
                if is_subgroup:
                    rows.extend(report["factMap"][i]["rows"]) 
        else:
            factMapKey = f"{group_key}!T"
            factMapEntry = report["factMap"][factMapKey]
            rows = factMapEntry["rows"]

        data = []
        for row in rows:
            row_data = []
            row_data.append(group["label"])
            for cell in row["dataCells"]:
                row_data.append(cell["label"])
            data.append(row_data)
        df2 = pd.DataFrame(data, columns = column_names)      
        df = pd.concat([df, df2], ignore_index = True)

    df["fetch_date"] = pd.Timestamp.now(tz='America/New_York').strftime("%Y-%m-%d")

    report_name = report["attributes"]["reportName"].replace(" ", "_")
    report_name = re.sub(r"(-)|(\.)|( -)|(_-)", "", report_name)

    upload_to_bigquery(report_name, df)

def pull_non_grouped_leadership_report(report_id, token):
    report = pull_report(report_id, token)
    if "reportMetadata" not in report:
        logging.critical(f"Could not pull {report_id}: {report[0]}")
        return

    column_names = report["reportMetadata"]["detailColumns"]
    column_names = [column.replace(".", "_") for column in column_names]
    factMapKey = "T!T"
    df = pd.DataFrame(columns = column_names)
    
    factMapEntry = report["factMap"][factMapKey]
    rows = factMapEntry["rows"] 
    data = []
    for row in rows:
        row_data = []
        for cell in row["dataCells"]:
            row_data.append(cell["label"])
        data.append(row_data)
    df = pd.DataFrame(data, columns = column_names)      

    df["fetch_date"] = pd.Timestamp.now(tz='America/New_York').strftime("%Y-%m-%d")
    report_name = report["attributes"]["reportName"].replace(" ", "_")

    upload_to_bigquery(report_name, df)

def pull_cross_grouping_leadership_report(report_id, token):
    report = pull_report(report_id, token)
    if "reportMetadata" not in report:
        logging.critical(f"Could not pull {report_id}: {report[0]}")
        return

    column_names = []
    [column_names.append(col["label"]) for col in report["groupingsAcross"]["groupings"]]
    group_column = report["reportMetadata"]["groupingsDown"][0]["name"]
    column_names.insert(0, group_column)
    column_names = [column.replace(".", "_") for column in column_names]
    column_names = [column.replace(" ", "_") for column in column_names]
    column_names = [column.replace("-", "_") for column in column_names]

    groups = report["groupingsDown"]["groupings"]
    df = pd.DataFrame(columns = column_names)
    
    data = []
    for group in groups:
        row_data = []
        row_data.append(group["label"])
        for cell in range(len(column_names)-1):
            factMapKey = f"{group['key']}!{cell}"
            factMapEntry = report["factMap"][factMapKey]
            cell = factMapEntry["aggregates"][0]["value"] 
            row_data.append(cell)
        data.append(row_data)
    df = pd.DataFrame(data, columns = column_names)      

    df["fetch_date"] = pd.Timestamp.now(tz='America/New_York').strftime("%Y-%m-%d")

    report_name = report["attributes"]["reportName"].replace(" ", "_")

    upload_to_bigquery(report_name, df)

def upload_to_bigquery(table, dframe):
    if len(dframe) == 0:
        logging.critical(f"Data is not available for {table}")
        return

    table_id = f"{cfg.project}.{cfg.dataset}.{table}"
    logging.info(f"Uploading data in BigQuery to {table_id}")

    client = bigquery.Client(project=cfg.project)
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = "WRITE_TRUNCATE" 

    # Upload and wait for job to complete
    job = client.load_table_from_dataframe(
        dframe, 
        table_id, 
        job_config=job_config
        )

    if job.result():
        logging.info(f"The table <{table_id}> successfully loaded.")
        
    if not job.result():
        logging.critical(f"The table <{table_id}> did not load successfully.")

def salesforce_reports(event, context):
    authentication = authenticate_salesforce()
    token = authentication["access_token"]

    for report in cfg.grouped_reports:
        pull_grouped_leadership_report(report, token) 

    for report in cfg.non_grouped_reports:
        pull_non_grouped_leadership_report(report, token)

    for report in cfg.cross_grouping_reports:
        pull_cross_grouping_leadership_report(report, token) 

if __name__ == "__main__":
    salesforce_reports("", "")
