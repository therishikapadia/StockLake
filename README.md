# StockLake
Stock Market Data Engineering Pipeline (Bronze-Silver-Gold)

## Overview
StockLake is an end-to-end stock market data engineering project built using the
Medallion Architecture. The pipeline ingests raw market data using Apache Kafka,
processes it through structured layers, and stores analytics-ready data in PostgreSQL.

This project is designed to reflect real-world data engineering practices.

## Architecture
Data Source -> Kafka -> Bronze -> Silver -> Gold -> PostgreSQL

## Pipeline Details

### Bronze Layer (Raw Data)
- Raw stock market data ingested through Kafka
- Data stored exactly as received
- No cleaning or transformations applied
- Used for traceability and replay

### Silver Layer (Clean Data)
- Removed duplicate records
- Standardized timestamps and data types
- Handled missing values
- Applied basic data validation checks

### Gold Layer (Analytics Data)
- Aggregated stock price data
- Calculated indicators such as returns and moving averages
- Prepared analytics-ready datasets

## Data Storage
- Bronze, Silver, and Gold layers stored in a data lake-style folder structure
- Final Gold layer data loaded into PostgreSQL
- Enables fast querying for analytics and dashboards

## Tech Stack
- Python
- Apache Kafka
- PostgreSQL
- Pandas
- Git and GitHub

## Key Highlights
- Industry-standard Bronze-Silver-Gold architecture
- Event-driven ingestion using Kafka
- Clean separation of raw, processed, and analytics data
- Analytics-ready storage in PostgreSQL

## Future Enhancements
- Real-time streaming analytics
- Data quality monitoring
- Dashboard integration
- Feature generation for machine learning pipelines

## Author
Rishi Kapadia
