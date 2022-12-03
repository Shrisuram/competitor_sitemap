from google.cloud import storage

project = "api-project-901373404215"
storage_client = storage.Client()
bucket = storage_client.get_bucket(project)

# Consumer Key
blob = bucket.blob('salesforce_client_id.txt')
client_id = blob.download_as_string().decode("utf-8")
# Consumer Secret
blob = bucket.blob('salesforce_client_secret.txt')
client_secret = blob.download_as_string().decode("utf-8")
# sf_user = your SFDC username
blob = bucket.blob('salesforce_email.txt')
sf_user = blob.download_as_string().decode("utf-8")
# sf_pass = your SFDC password
blob = bucket.blob("salesforce_password.txt")
sf_pass = blob.download_as_string().decode("utf-8")

login_url = "https://login.salesforce.com/services/oauth2/token"
salesforce_report_url = "https://forbes.my.salesforce.com/services/data/v29.0/analytics/reports"
grant_type = "password"
api_version = "4"
dataset = "Salesforce_leadership"

grouped_reports = [
    "00O3m000008rT92EAE",
    "00O3m000008rVW3EAM",
    "00O3m000008rU5aEAE",
    "00O3m000008rVS1EAM",
    "00O3m000008rVPbEAM",
    "00O3m000008rUViEAM",
    "00O3m000008rSsaEAE",
    "00O3m000008rRq4EAE",
    "00O3m000008rKjuEAE"
]

non_grouped_reports = [
    "00O3m000008rRauEAE"
]

cross_grouping_reports = [
    "00O3m000008rVPWEA2"
]
