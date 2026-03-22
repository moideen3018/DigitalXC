# DigitalXC ITSM Data Pipeline

An end-to-end data engineering project for transforming raw IT service management ticket data into reliable, analysis-ready datasets and interactive operational dashboards.

This project demonstrates how to build a modern analytics pipeline using **PostgreSQL**, **dbt**, **Apache Airflow**, and **Apache Superset**. It covers the full lifecycle from raw data ingestion and transformation to orchestration, validation, and business-facing visualization.

---

## Project Summary

The goal of this project is to process raw ticket dump data and convert it into meaningful operational insights for support and service teams. The pipeline ingests raw ticket data into PostgreSQL, transforms it with dbt, orchestrates workflow execution with Airflow, and exposes KPIs through Superset dashboards.

This project is designed to reflect a practical analytics engineering / data engineering use case where stakeholders need visibility into:

- ticket volume trends
- open vs resolved ticket distribution
- priority-wise workload
- response and resolution performance
- backlog and operational efficiency

---

## Business Problem

Support teams often work with raw ticket exports that are inconsistent, hard to query, and not suitable for reporting directly. Without a structured pipeline, it becomes difficult to answer basic operational questions such as:

- How many tickets are being created over time?
- What is the current backlog?
- Which priority levels are driving the most workload?
- How efficiently are tickets being resolved?
- Are there trends that indicate SLA or process issues?

This project solves that problem by building a reusable pipeline that standardizes ticket data and turns it into trusted datasets for reporting and decision-making.

---

## Architecture Overview

**Pipeline flow:**

Raw Ticket Dump → PostgreSQL Staging → dbt Transformations → Airflow Orchestration & Validation → Superset Dashboard

### High-level components

- **PostgreSQL** stores both raw and transformed ticket data.
- **dbt** performs cleaning, modeling, and aggregation.
- **Apache Airflow** schedules and orchestrates the pipeline.
- **Apache Superset** presents the final KPIs and trends through dashboards.

---

## Core Features

### 1. Data Ingestion
- Loads raw ticket dump data into PostgreSQL staging tables.
- Creates a structured foundation for downstream transformations.

### 2. Data Transformation with dbt
- Cleans and standardizes raw ticket data.
- Handles inconsistent values, nulls, and duplicates where applicable.
- Builds transformed analytical tables for reporting.
- Creates aggregated models for dashboard consumption.

### 3. Workflow Orchestration with Airflow
- Automates the pipeline execution flow.
- Ensures transformation steps run in the correct order.
- Supports validation and monitoring as part of scheduled runs.

### 4. Data Visualization with Superset
- Exposes operational ticket insights in dashboard form.
- Enables quick exploration of ticket KPIs and trends.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| **PostgreSQL** | Stores raw, staging, and transformed ticket datasets |
| **dbt** | Performs SQL-based transformation, modeling, and testing |
| **Apache Airflow** | Orchestrates and schedules pipeline tasks |
| **Apache Superset** | Builds interactive dashboards for business users |

---

## Data Modeling Approach

The project follows a layered transformation approach:

### Staging Layer
Used to clean and standardize raw source data before business logic is applied.

Typical staging tasks include:
- renaming columns for consistency
- standardizing status and priority values
- handling missing or malformed fields
- removing obvious duplicates

### Analytics / Reporting Layer
Used to create business-facing datasets that power dashboards.

Typical reporting outputs include:
- ticket summary tables
- ticket counts by status
- ticket counts by priority
- daily / weekly / monthly ticket trends
- resolution performance metrics

---

## Example KPIs Tracked

The Superset dashboard can be used to monitor metrics such as:

- Total tickets
- Open tickets
- Resolved tickets
- Tickets by priority
- Tickets by status
- Ticket creation trend over time
- Average resolution time
- Backlog volume

These KPIs help teams understand workload, identify bottlenecks, and improve service performance.

---

## Project Structure

```bash
DigitalXC-ITSM-Data-Pipeline/
│
├── airflow/                # DAGs and orchestration logic
├── dbt/                    # dbt models, tests, and project configuration
├── sql/                    # SQL scripts for setup or helper queries
├── dashboards/             # Superset assets or dashboard references
├── data/                   # Raw input data or sample ticket dumps
├── docs/                   # Screenshots, architecture diagram, notes
└── README.md               # Project documentation
```

> Adjust the folder names above if your actual repository structure differs.

---

## How the Pipeline Works

1. Raw ticket dump is loaded into PostgreSQL.
2. dbt staging models clean and standardize source fields.
3. dbt transformation models create reporting-ready datasets.
4. Airflow triggers and orchestrates the pipeline steps.
5. Validation checks confirm expected pipeline execution.
6. Superset consumes transformed tables to build dashboards.

---

## Setup Instructions

### Prerequisites
Make sure the following are installed:

- PostgreSQL
- Python 3.x
- dbt
- Apache Airflow
- Apache Superset

### 1. Clone the repository
```bash
git clone <your-repository-url>
cd DigitalXC-ITSM-Data-Pipeline
```

### 2. Configure PostgreSQL
- Create a database for the project.
- Update connection credentials in your dbt and Airflow configurations.

### 3. Run dbt models
```bash
cd dbt
dbt deps
dbt run
dbt test
```

### 4. Start Airflow
```bash
airflow standalone
```
Then enable the DAG responsible for orchestrating the ITSM pipeline.

### 5. Launch Superset
Start Superset and connect it to the transformed PostgreSQL schema used by the project.

---

## Data Quality and Validation

To make the pipeline more reliable, validation checks should be included at transformation level and orchestration level.

Recommended checks:

- uniqueness tests on ticket identifiers
- not-null tests on critical columns
- accepted-value tests for status and priority fields
- row-count comparisons between source and transformed layers
- task-level monitoring in Airflow for pipeline failures

If implemented, these checks improve trust in reporting outputs and make the project more production-oriented.

---

## What This Project Demonstrates

This project highlights practical skills relevant to data engineering and analytics engineering roles:

- SQL-based data transformation
- dimensional / reporting-oriented data modeling
- workflow orchestration
- dashboard enablement for business users
- data quality awareness
- end-to-end ownership of a reporting pipeline

---

## Recommended Enhancements

To make the repository even stronger for recruiters and hiring managers, consider adding:

- architecture diagram
- Airflow DAG screenshot
- Superset dashboard screenshots
- sample source schema and transformed schema
- documented dbt tests
- Docker setup for easier local execution
- CI/CD pipeline for automated validation
- incremental loading for larger datasets

---

## Suggested Screenshots to Add

Place these inside a `docs/` folder and reference them here:

- Airflow DAG view
- dbt model lineage graph
- Superset dashboard overview
- sample KPI charts

Example markdown:

```md
![Airflow DAG](docs/airflow_dag.png)
![Superset Dashboard](docs/superset_dashboard.png)
```

---

## Resume / Portfolio Value

This repository can be presented as an end-to-end analytics pipeline project that demonstrates the ability to:

- ingest raw operational data
- transform it into trusted analytical models
- orchestrate workflows reliably
- expose insights for decision-making

That makes it especially relevant for roles such as:

- Data Engineer
- Analytics Engineer
- BI Engineer
- Reporting / ETL Developer

---

## Future Improvements

- Add automated source ingestion instead of manual dump loading
- Introduce incremental dbt models
- Add alerting for failed Airflow runs
- Containerize the stack using Docker Compose
- Expand dashboard coverage with SLA and assignee-level metrics

---

## Author

**Mohamed Mohaideen Ahamed Nizar**

If you are using this project as part of your job search portfolio, consider pinning this repository on GitHub and adding screenshots for stronger visual impact.
