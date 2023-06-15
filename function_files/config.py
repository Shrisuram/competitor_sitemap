# Configuration file for bi_data_alerts

from google.cloud import bigquery

# Main.py references the following elements:

# -bucket_name
# -file_name
# -scopes
# -project_id
# -spreadsheet ids
# -sheet names
# -value render options
# -col names
# -SQL queries

bucket_name = "api-project-901373404215"
file_name = "credentials.json"
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
project_id = "api-project-901373404215"

columns = {0: "Site", 1: "URL"}

competitor_sitemap_id = "1QPjn7YykAv_DhUwmmb6sLphXMuh2LSTxAwvg86yVPkM"
sheet_name = "Sitemap_list"

value_render_option = "UNFORMATTED_VALUE"
date_time_render_option = "FORMATTED_STRING"

dataset = 'Sitemap'

NYT = [
bigquery.SchemaField('loc', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('lastmod', 'TIMESTAMP',mode = 'NULLABLE'),
bigquery.SchemaField('news', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_publication', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('publication_name', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('publication_language', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_publication_date', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_title', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_keywords', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('image', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('image_loc', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('sitemap', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('etag', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('sitemap_last_modified', 'TIMESTAMP',mode = 'NULLABLE'),
bigquery.SchemaField('sitemap_size_mb', 'FLOAT',mode = 'NULLABLE'),
bigquery.SchemaField('download_date', 'TIMESTAMP',mode = 'NULLABLE'),
]
WaPo = [
bigquery.SchemaField('loc', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('lastmod', 'TIMESTAMP',mode = 'NULLABLE'),
bigquery.SchemaField('news', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_publication', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('publication_name', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('publication_language', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_publication_date', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_title', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('changefreq', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('sitemap', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('sitemap_size_mb', 'FLOAT',mode = 'NULLABLE'),
bigquery.SchemaField('download_date', 'TIMESTAMP',mode = 'NULLABLE'),
bigquery.SchemaField('news_keywords', 'STRING',mode = 'NULLABLE'),
]
Guardian = [
bigquery.SchemaField('loc', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('lastmod', 'TIMESTAMP',mode = 'NULLABLE'),
bigquery.SchemaField('image', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('image_loc', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('changefreq', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_publication', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('publication_name', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('publication_language', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_publication_date', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_title', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_keywords', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_genres', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('sitemap', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('etag', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('sitemap_size_mb', 'FLOAT',mode = 'NULLABLE'),
bigquery.SchemaField('download_date', 'TIMESTAMP',mode = 'NULLABLE'),
]
WSJ = [
bigquery.SchemaField('loc', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('lastmod', 'TIMESTAMP',mode = 'NULLABLE'),
bigquery.SchemaField('news', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_publication', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('publication_name', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('publication_language', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_publication_date', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_title', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('image', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('image_loc', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('news_keywords', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('priority', 'FLOAT',mode = 'NULLABLE'),
bigquery.SchemaField('changefreq', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('sitemap', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('etag', 'STRING',mode = 'NULLABLE'),
bigquery.SchemaField('sitemap_last_modified', 'TIMESTAMP',mode = 'NULLABLE'),
bigquery.SchemaField('sitemap_size_mb', 'FLOAT',mode = 'NULLABLE'),
bigquery.SchemaField('download_date', 'TIMESTAMP',mode = 'NULLABLE'),
]
