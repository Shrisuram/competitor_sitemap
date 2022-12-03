# Salesforce Leadership Reports

This cloud function pulls the data of Salesforce leadership reports listed in [this sheet](https://docs.google.com/spreadsheets/d/1qeluE-17s5LItyC09fvZZZ6N5f32PQZoFRkZSW4fgIw/edit#gid=619098472).

## Frequency

This cloud function is triggered by a PubSub topic which runs according to [this cloud scheduler job](https://console.cloud.google.com/cloudscheduler/jobs/edit/us-central1/salesforce_reports?authuser=1&project=api-project-901373404215&supportedpurview=project)

## Inputs

[Salesforce leadership reports Ids](https://docs.google.com/spreadsheets/d/1qeluE-17s5LItyC09fvZZZ6N5f32PQZoFRkZSW4fgIw/edit#gid=619098472)

## Outputs

Update the table for each report every day upon fetch. 

## Owner

This repository is actively maintained by the Data Engineering Team. Send us an email at [dataengineering@forbes.com](mailto:dataengineering@forbes.com)

Slack Contacts:
- Samar Al-Shboul (@Samar Al-Shboul)
- Kelsey Simmons (@Kelsey Simmons)