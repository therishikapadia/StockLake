from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

spark = SparkSession.builder \
    .appName("SilverStockCleaner") \
    .getOrCreate()

schema = StructType([
    StructField("symbol", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("timestamp", TimestampType(), True),
])

bronze_df = spark.read.parquet("storage/bronze/stock_prices")

silver_df = bronze_df \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*") \
    .dropna()

silver_df.write \
    .mode("overwrite") \
    .parquet("storage/silver/stock_prices_clean")

spark.stop()
