# DigitalXC ITSM Data Pipeline

This project implements a data pipeline for analyzing ticket data, from ingestion and transformation to visualization.  It leverages several tools including DBT, PostgresDB, Apache Airflow, and Apache Superset.

## Project Overview

The pipeline processes a ticket dump, performs transformations, and presents key metrics in an interactive dashboard.  The following tasks are implemented:

1. **Data Ingestion and Transformation (DBT & PostgresDB):** The raw ticket data is loaded into a Postgres database.  DBT is used to perform data cleaning and transformations, creating aggregated tables for analysis.

2. **Workflow Orchestration (Apache Airflow):** Airflow orchestrates the entire pipeline, from data ingestion to triggering DBT transformations and validation.

3. **Data Visualization (Apache Superset):** Superset is used to create an interactive dashboard displaying key ticket metrics and trends.

## Technologies Used

* **PostgresDB:**  Database for storing the raw and transformed ticket data.
* **DBT (Data Build Tool):**  For data transformation and modeling.
* **Apache Airflow:**  For workflow orchestration and scheduling.
* **Apache Superset:**  For data visualization and dashboarding.