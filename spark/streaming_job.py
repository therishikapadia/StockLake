from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from schema import stock_schema


spark = SparkSession.builder \
    .appName("StockKafkaStreaming") \
    .getOrCreate()

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "stock_prices") \
    .option("startingOffsets", "latest") \
    .load()

parsed_df = kafka_df.selectExpr("CAST(value AS STRING)")

query = parsed_df.writeStream \
    .format("parquet") \
    .option("path", "storage/bronze/stock_prices") \
    .option("checkpointLocation", "storage/checkpoints/bronze_stock_prices") \
    .outputMode("append") \
    .start()

query.awaitTermination()   # 🔴 THIS IS NON-NEGOTIABLE
