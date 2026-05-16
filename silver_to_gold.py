from pyspark.sql import SparkSession 

spark = SparkSession.builder.appName("SilvertoGold_SparkSQL").getOrCreate()

silver_path = "local_datalake/silver/cleaned_data"

df_silver = spark.read.parquet(silver_path)

mapping_path = "local_datalake/bronze/region_mapping.csv"

df_mapping = spark.read.option("header", "true").csv(mapping_path)

df_silver.createOrReplaceTempView("transactions")
df_mapping.createOrReplaceTempView("regions")

sql_query = """
    SELECT transactions.location, regions.region, regions.manager, COUNT(*) as total_events
    FROM transactions JOIN regions ON transactions.location =  regions.location
    GROUP BY transactions.location, regions.region, regions.manager
"""
df_gold = spark.sql(sql_query)

gold_path = "local_datalake/gold/business_summary"
df_gold.write.mode("overwrite").option("header", "True").csv(gold_path)

print("gold waas updated by spark sql")
spark.stop()






# silver_path = "local_datalake/silver/cleaned_data"
# df_silver = spark.read.parquet(silver_path)
# df_gold = df_silver.groupBy("location").count()

# gold_path = "local_datalake/gold/business_summary"

# df_gold.write.mode("overwrite").option("header", "true").csv(gold_path)

# print('we saved correctly in gold')
# spark.stop()