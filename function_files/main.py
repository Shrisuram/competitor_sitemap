import json
import logging


from google.cloud.bigquery.client import Client
import google.cloud.logging
import config as cfg
import google.cloud.logging
import pandas as pd
from google.cloud import bigquery, storage
from google.oauth2 import service_account
from googleapiclient import discovery
import advertools as adv

# Setup Logging
logging.basicConfig(
    format="%(asctime)s:%(levelname)s-%(lineno)d-%(message)s", level=logging.INFO
)
logging_client = google.cloud.logging.Client()
logging_client.setup_logging()

# Instantiate BQ Client
bq_client = bigquery.Client(project=cfg.project_id)

# Get credentials from GCS to fetch Google Spreadsheets
storage_client = storage.Client()
bucket = storage_client.get_bucket(cfg.bucket_name)
blob = bucket.blob(cfg.file_name)

KEY_FILE_STR2 = blob.download_as_string()
KEY_FILE2 = json.loads(KEY_FILE_STR2)

scopes = cfg.scopes
credentials = service_account.Credentials.from_service_account_info(
    KEY_FILE2, scopes=scopes
)

service = discovery.build(
    "sheets", "v4", credentials=credentials, cache_discovery=False
)


def get_spreadsheet_data(
    spreadsheet_id: str, sheet_name: str, sheet_range: str, column_names: dict = None
) -> pd.DataFrame:
    """
    Returns data from passed spreadsheet as a pandas dataframe
    """

    logging.info(f"Getting data from {sheet_name}")

    req = (
        service.spreadsheets()
        .values()
        .batchGet(
            spreadsheetId=spreadsheet_id,
            ranges=[sheet_name + sheet_range],
            valueRenderOption=cfg.value_render_option,
            dateTimeRenderOption=cfg.date_time_render_option,
            majorDimension="COLUMNS",
        )
    )

    resp = req.execute()["valueRanges"]
    
    sheet_df = pd.DataFrame(data=resp[0]["values"]).T
    if column_names:
        sheet_df.rename(columns=column_names, inplace=True)
    sites = sheet_df['Site'].tolist()
    sitemaps = sheet_df['URL'].tolist()
    return sites, sitemaps



def bq_load(df: pd.DataFrame, dataset: str, table_id: str, schema = None):
    
#     """ Function to facilitate load to BigQuery. 
#         Accepts data frame as parameter. """ 
    
    logging.info(f"Uploading to BQ Table {table_id}")
    dataset_ref = bq_client.dataset(dataset)
    table_ref = dataset_ref.table(table_id)

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.allow_quoted_newlines = True
    if schema:
        job_config.schema = schema
        job_config.autodetect = False
    else:
        job_config.autodetect = True
    job_config.ignore_unknown_values = True

    job = bq_client.load_table_from_dataframe(
        df, table_ref, location="US", job_config=job_config
    )

    return job.result()




def sitemap_parse(event,context):
    sites, sitemaps = get_spreadsheet_data(cfg.competitor_sitemap_id, cfg.WSJ_sheet_name, "!A2:D", cfg.columns)
    for site_index in range(len(sitemaps)):
        economist =  adv.sitemap_to_df(sitemaps[site_index])
        table_id = sites[site_index]
        bq_load(economist, cfg.dataset, table_id)



if __name__ == "__main__":
    sitemap_parse("","")
