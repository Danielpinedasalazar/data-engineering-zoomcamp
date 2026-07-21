# Module 2: Workflow Orchestration

NY Taxi data pipelines orchestrated with [Kestra](https://kestra.io/), progressing from a basic script to scheduled, deduplicated loads into Postgres and GCS/BigQuery.

## Flows

| File | What it does |
|------|---------------|
| [`02_pyton.yaml`](flows/02_pyton.yaml) | Hello-world flow: runs a Python script in Docker to fetch Docker Hub download stats for the Kestra image. |
| [`03_getting_started_data_pipeline.yaml`](flows/03_getting_started_data_pipeline.yaml) | Extracts JSON from an API, transforms it with a Python script, and queries it with DuckDB. |
| [`04_postgres_taxi.yaml`](flows/04_postgres_taxi.yaml) | Downloads a NY taxi CSV (taxi type/year/month selectable), loads it into Postgres via a staging table, dedupes with a hashed row id. |
| [`05_postgres_taxi_scheduled.yaml`](flows/05_postgres_taxi_scheduled.yaml) | Same as above, but driven by a monthly schedule trigger instead of manual inputs. |
| [`06_gcp_kv.yaml`](flows/06_gcp_kv.yaml) | One-off flow that sets GCP project/location/bucket/dataset as Kestra KV pairs, reused by later flows. |
| [`07_gcp_setup.yaml`](flows/07_gcp_setup.yaml) | Provisions the GCS bucket and BigQuery dataset used by the pipeline. |
| [`08_gcp_taxi.yaml`](flows/08_gcp_taxi.yaml) | Uploads taxi CSVs to GCS, loads them into BigQuery through an external table, and merges into a partitioned table using a hashed row id to avoid duplicates. |
| [`09_gcp_taxi_scheduled.yaml`](flows/09_gcp_taxi_scheduled.yaml) | Scheduled version of `08`: separate cron triggers for green (day 1, 09:00) and yellow (day 1, 10:00) monthly loads. |

## How to run

1. Start Postgres + pgAdmin + Kestra:

   ```bash
   cd ny_taxi_postgres_data
   docker compose up -d
   ```

   Optionally set your own Kestra login before starting it, otherwise it defaults to `admin@example.com` / `changeme`:

   ```bash
   export KESTRA_USER=you@example.com
   export KESTRA_PASSWORD=your-password
   docker compose up -d
   ```

2. Open the Kestra UI at [localhost:8080](http://localhost:8080) and log in with the credentials above.
3. Open pgAdmin at [localhost:8085](http://localhost:8085) (`admin@admin.com` / `root`) to inspect loaded data, connecting to host `pgdatabase`, user `root`, password `root`, db `ny_taxi`.
4. In the Kestra UI, create each flow under **Flows** by pasting in the YAML from `flows/`, in numeric order (later flows depend on KV values / resources set up by earlier ones).
5. For the GCP flows (`06`–`09`) you'll need:
   - A GCP service account key stored as the Kestra secret `GCP_CREDS`.
   - `06_gcp_kv.yaml` run once first, with your own bucket name (must be globally unique) and project id filled in.
   - `07_gcp_setup.yaml` run once to create the bucket and BigQuery dataset.
6. Execute `04`/`08` manually (pick taxi/year/month), or add the `05`/`09` flows and let their schedule triggers backfill/run automatically.
