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
WSJ_sheet_name = "WSJ"

value_render_option = "UNFORMATTED_VALUE"
date_time_render_option = "FORMATTED_STRING"

dataset = 'Shri_test'
