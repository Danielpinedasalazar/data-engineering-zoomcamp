variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my-creds.json"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "project" {
  description = "Project"
  default     = "terraform-demo-503015"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bg_dataset_name" {
  description = "My Big Query Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "terraform-demo-503015-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}