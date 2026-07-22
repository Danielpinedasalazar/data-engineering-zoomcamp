"""Loads NYC TLC green/yellow trip data (Jan 2019) into the local DuckDB `prod` schema.

Source: official NYC TLC public parquet files (cloudfront), matching the
dev_start_date/dev_end_date window used by the staging models.
"""
import duckdb

DUCKDB_PATH = "taxi_rides_ny.duckdb"
SOURCE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/{table}_tripdata_2019-01.parquet"

TABLES = ["green", "yellow"]

con = duckdb.connect(DUCKDB_PATH)
con.execute("create schema if not exists prod")

for table in TABLES:
    url = SOURCE_URL.format(table=table)
    con.execute(f"""
        create or replace table prod.{table}_tripdata as
        select * from read_parquet('{url}')
    """)
    count = con.execute(f"select count(*) from prod.{table}_tripdata").fetchone()[0]
    print(f"Loaded prod.{table}_tripdata: {count} rows")

con.close()
