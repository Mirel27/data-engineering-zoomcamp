## Data Engineering Zoomcamp - Learning Project

Project status: In progress.

This is a learning repo where I am building an end-to-end data engineering workflow step by step.

![Simple workflow](image.png)

## Architecture

Data source (NYC taxi CSV) -> Python ingest script -> PostgreSQL -> pgAdmin

## Why Docker + venv

`venv` isolates Python packages for one project, but still uses the host OS.
Docker isolates the full runtime environment (OS layer, Python, packages, code).

## Why Docker Compose

Docker Compose lets this project start multiple services together with one command.
It keeps service names, networks, ports, and volumes in one file so the setup is reproducible and easier to run.

## Quickstart (5 Commands)

```bash
cd /workspaces/data-engineering-zoomcamp/pipeline
docker compose up -d
docker build -t taxi_ingest:v001 .
docker run -it --network=pipeline_default taxi_ingest:v001 --pg-user=root --pg-pass=root --pg-host=pgdatabase --pg-port=5432 --pg-db=ny_taxi --target-table=yellow_taxi_trips_2021_1 --chunksize=100000
uv run pgcli -h localhost -p 5433 -u root -d ny_taxi
```

## Local Development

Use this interpreter in VS Code:

`/workspaces/data-engineering-zoomcamp/pipeline/.venv/bin/python`

Run local scripts with:

```bash
cd /workspaces/data-engineering-zoomcamp/pipeline
uv run python ingest_data.py --help
```

## Roadmap

- [x] Containerized PostgreSQL setup
- [x] Parameterized ingestion script with Click
- [x] Docker image for ingestion job
- [x] Docker Compose for Postgres + pgAdmin
- [ ] Add logging and retry handling
- [ ] Add data quality checks
- [ ] Add tests for ingestion flow
- [ ] Add orchestration (Airflow/Prefect)
- [ ] Add CI pipeline
