# Terraform (GCP)

Provisions a GCS bucket and a BigQuery dataset on GCP.

## Setup

1. Create a GCP service account key and save it as `keys/my-creds.json` (this path is gitignored — never commit it).
2. Update `project` in `variables.tf` with your own GCP project id.
3. Run:
   ```
   terraform init
   terraform plan
   terraform apply
   ```
