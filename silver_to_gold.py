from pyspark.sql import SparkSession 

spark = SparkSession.builder.appName("SilvertoGoldPipeline").getOrCreate()

silver_path = "local_datalake/silver/cleaned_data"
df_silver = spark.read.parquet(silver_path)
df_gold = df_silver.groupBy("location").count()

gold_path = "local_datalake/gold/business_summary"

df_gold.write.mode("overwrite").option("header", "true").csv(gold_path)

print('we saved correctly in gold')
spark.stop()