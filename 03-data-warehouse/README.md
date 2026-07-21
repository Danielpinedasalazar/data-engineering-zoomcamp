# Module 3: Data Warehouse (BigQuery)

This module was done entirely in the BigQuery console/SQL editor rather than local scripts, so there's no code to run here — this README is a summary of what it covered.

Using the green/yellow taxi tables loaded into BigQuery in [module 2](../02-workflow-orchestration), the work covered:

- **Partitioning and clustering** — comparing a partitioned-by-pickup-date table against a non-partitioned one, and adding clustering on top, to see the effect on bytes scanned and query cost.
- **BigQuery internals** — how BigQuery's columnar storage and query execution explain those performance differences.
- **Best practices** — filtering/clustering columns, avoiding `SELECT *`, and other patterns that reduce cost and improve query speed.
- **BigQuery ML** — training and evaluating a simple model (e.g. tip prediction) directly with `CREATE MODEL` / `ML.EVALUATE` / `ML.PREDICT` SQL, without exporting data out of BigQuery.

No credentials or project-specific SQL are checked in here since queries were run ad hoc against a personal GCP project in the console.
