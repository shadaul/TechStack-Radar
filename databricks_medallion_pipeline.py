# Databricks notebook source
import requests
import json

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

file_path = "/Volumes/workspace/default/bronze_zone/raw_data.json"
with open(file_path, "w") as file:
    file.write(response.text)

# COMMAND ----------

file_path = "/Volumes/workspace/default/bronze_zone/raw_data.json" 

df_bronze = spark.read.option("multiline", "true").json(file_path)

display(df_bronze)

# COMMAND ----------

df_silver = df_bronze.dropna()
print(f"strok v bronze {df_bronze.count()}")
print(f"strok v silver {df_silver.count()}")

silver_path = "/Volumes/workspace/default/bronze_zone/silver_data"
df_silver.write.format("parquet").mode("overwrite").save(silver_path)
print(f"uspeshno saved v {silver_path}")

display(silver_path)

# COMMAND ----------

df_gold = spark.read.parquet("/Volumes/workspace/default/bronze_zone/silver_data")

df_gold = df_gold.groupBy("company_name").count().withColumnRenamed("count", "vacancies_count").orderBy("vacancies_count", ascending=False)

display(df_gold)

# COMMAND ----------

df_gold.write.format("delta").mode("overwrite").saveAsTable("default.top_companies")

print("Архитектура Medallion завершена! SQL-таблица top_companies создана и готова к работе.")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT company_name, vacancies_count 
# MAGIC FROM default.top_companies
# MAGIC WHERE vacancies_count >= 5;

# COMMAND ----------

