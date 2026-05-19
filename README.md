# TechStack Radar: Automated Databricks Medallion Pipeline

## Overview
This repository contains an end-to-end Data Engineering pipeline built on Databricks. The project implements the Medallion Architecture to ingest raw job vacancy data, clean it, and aggregate it into a structured format ready for business intelligence tools and analytical queries.

## Architecture: The Medallion Approach
The data processing pipeline is structured into three distinct layers to ensure data quality, scalability, and optimized query performance:

* **Bronze Layer (Raw Data Ingestion):** Raw data is provided in multiline JSON format. The pipeline utilizes PySpark to read this semi-structured data directly from Databricks Volumes, establishing the initial schema without modifying or losing any source information.
* **Silver Layer (Cleansing and Transformation):** The raw data undergoes validation and cleansing. Missing values and null records are filtered out using PySpark transformations. The refined data is then written back to the storage layer in columnar Apache Parquet format, which drastically reduces the storage footprint and improves read operations.
* **Gold Layer (Business Aggregations):** The cleaned Parquet data is aggregated to extract direct business value. In this specific pipeline, the data is grouped by company name to calculate the total number of vacancies per company and sorted to identify top employers. The final output is saved as a managed Delta Table, providing ACID transactions, versioning, and serving as a robust, production-ready source for SQL querying.

## Automation and Orchestration
The execution of the data pipeline is fully automated for daily production use using Databricks Workflows (Jobs).
* **Compute Model:** The job utilizes Databricks Serverless compute. This ensures instant resource allocation when the pipeline triggers and immediate termination upon completion, optimizing cloud infrastructure costs.
* **Scheduling:** The pipeline is configured with a time-based trigger, scheduled to run automatically every day at 06:00 AM (Europe/Warsaw timezone) to process the latest batch of data.

## Technologies Used
* **Databricks:** Workspace, Unity Catalog, Databricks Workflows
* **Apache Spark:** PySpark API for distributed data processing
* **Storage Formats:** Delta Lake, Apache Parquet, JSON
* **Languages:** Python, SQL
* **Version Control:** Git, GitHub

## Repository Files
* `databricks_medallion_pipeline.py`: The core pipeline script exported from the Databricks notebook environment. It contains the sequential logic for reading the raw JSON, processing it through the Medallion layers, and registering the final Delta table.
* `local_datalake/`: The local directory structure (simulating the cloud volume) used for initial data storage and testing of the raw data files before cloud deployment.
