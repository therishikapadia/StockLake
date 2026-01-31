\section*{StockLake}
Stock Market Data Engineering Pipeline using Bronze--Silver--Gold Architecture

\section*{Overview}
StockLake is an end-to-end stock market data engineering project that implements the Medallion Architecture.
Raw market data is ingested using Apache Kafka, processed through structured layers, and stored in PostgreSQL
for analytics and querying.

\section*{Architecture}
\[
\text{Data Source} \rightarrow \text{Kafka} \rightarrow \text{Bronze} \rightarrow \text{Silver} \rightarrow \text{Gold} \rightarrow \text{PostgreSQL}
\]

\section*{Pipeline Layers}
\textbf{Bronze Layer:} Raw stock market data ingested via Kafka without transformations.

\textbf{Silver Layer:} Cleaned and validated data with duplicates removed, standardized timestamps, and proper data types.

\textbf{Gold Layer:} Aggregated and analytics-ready datasets with indicators such as returns and moving averages.

\section*{Tech Stack}
Python, Apache Kafka, PostgreSQL, Pandas, Git

\section*{Highlights}
Industry-standard Medallion Architecture, event-driven ingestion using Kafka, and analytics-ready storage in PostgreSQL.

\section*{Author}
Rishi Kapadia
