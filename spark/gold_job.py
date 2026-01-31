from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, min, max, count

spark = SparkSession.builder \
    .appName("GoldStockAggregates") \
    .getOrCreate()

silver_df = spark.read.parquet("storage/silver/stock_prices_clean")

gold_df = silver_df.groupBy("symbol").agg(
    avg("price").alias("avg_price"),
    min("price").alias("min_price"),
    max("price").alias("max_price"),
    count("*").alias("record_count")
)

gold_df.write \
    .mode("overwrite") \
    .parquet("storage/gold/stock_metrics")

spark.stop()
