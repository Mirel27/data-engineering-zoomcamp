#!/usr/bin/env python
# coding: utf-8


import click
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

@click.command()
@click.option("--year", default=2021, type=int, show_default=True)
@click.option("--month", default=1, type=int, show_default=True)
@click.option("--pg-user", default="root", show_default=True)
@click.option("--pg-pass", default="root", show_default=True)
@click.option("--pg-host", default="localhost", show_default=True)
@click.option("--pg-port", default=5432, type=int, show_default=True)
@click.option("--pg-db", default="ny_taxi", show_default=True)
@click.option("--chunksize", default=100000, type=int, show_default=True)
@click.option("--target-table", default="yellow_taxi_data", show_default=True)
def run(year, month, pg_user, pg_pass, pg_host, pg_port, pg_db, chunksize, target_table):
    # Read a sample of the data
    prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/"


    dtype = {
        "VendorID": "Int64",
        "passenger_count": "Int64",
        "trip_distance": "float64",
        "RatecodeID": "Int64",
        "store_and_fwd_flag": "string",
        "PULocationID": "Int64",
        "DOLocationID": "Int64",
        "payment_type": "Int64",
        "fare_amount": "float64",
        "extra": "float64",
        "mta_tax": "float64",
        "tip_amount": "float64",
        "tolls_amount": "float64",
        "improvement_surcharge": "float64",
        "total_amount": "float64",
        "congestion_surcharge": "float64"
    }

    parse_dates = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime"
    ]

    engine = create_engine(
        f"postgresql+psycopg2://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}"
    )


    df_iter = pd.read_csv(
        prefix + f"yellow_tripdata_{year}-{month:02d}.csv.gz",
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunksize,
    )

    first = True
    for df in tqdm(df_iter):
        if first:
            df.head(n=0).to_sql(name=target_table, con=engine, if_exists="replace")
            first = False
        df.to_sql(name=target_table, con=engine, if_exists="append")


if __name__ == "__main__":
    run()




