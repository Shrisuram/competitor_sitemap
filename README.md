# Competitor-Sitemap
A sitemap is a blueprint of your website that help search engines find, crawl and index all of your website’s content. Sitemaps also tell search engines which pages on your site are most important.
This Script run in the [Competitor-Sitemap](https://console.cloud.google.com/functions/details/us-central1/competitor-sitemap?env=gen1&authuser=0&project=api-project-901373404215) Cloud Function to get the Sitemap Data using advertools package.
This cloud function pulls the data of URL for Sitemap from this [sheet](https://docs.google.com/spreadsheets/d/1qeluE-17s5LItyC09fvZZZ6N5f32PQZoFRkZSW4fgIw/edit#gid=619098472)

## Frequency

This cloud function is triggered by a PubSub topic which runs according to [this cloud scheduler job](https://console.cloud.google.com/cloudscheduler/jobs/edit/us-central1/competitor-sitemap?project=api-project-901373404215)

## Inputs

[Sites Sheet](https://docs.google.com/spreadsheets/d/1qeluE-17s5LItyC09fvZZZ6N5f32PQZoFRkZSW4fgIw/edit#gid=619098472)

## Outputs

Update the tables:
1. NYT
2. WaPo
3. Guardian
4. WSJ

## Directory Structure

### .github/workflows

- main.yml: Build file for the Cloud Function Deployment. 

### function_files

- main.py: Source code for the extracting and Uploding GSC data to BigQuery.
- config.py: Config Variables for Source Code(main.py) to use.
- requirements.txt: Contains Dependencies for the Source Code.

### README.md

## Owner

This repository is actively maintained by the Data Engineering Team. Send us an email at [dataengineering@forbes.com](mailto:dataengineering@forbes.com)

Slack Contacts:
- Shriniwas Suram(@Shrisuram)
- Zach Quinn (@zquinn)
- Kelsey Simmons (@Kelsey Simmons)
