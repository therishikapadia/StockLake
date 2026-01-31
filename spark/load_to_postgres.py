from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("LoadGoldToPostgres") \
    .getOrCreate()

gold_df = spark.read.parquet("storage/gold/stock_metrics")

gold_df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://stonks-postgres-1:5432/stock_dw") \
    .option("dbtable", "stock_metrics") \
    .option("user", "stock_user") \
    .option("password", "stock_pass") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

spark.stop()
