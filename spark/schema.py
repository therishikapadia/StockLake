from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType, TimestampType
stock_schema = StructType([
    StructField("symbol", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("high", DoubleType(), True),
    StructField("low", DoubleType(), True),
    StructField("volume", IntegerType(), True),
    StructField("timestamp", StringType(), True),
    StructField("ingested_at", StringType(), True)
])
