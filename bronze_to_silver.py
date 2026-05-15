from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName('BronzeToSilverPipeline').getOrCreate()

print("spark session running")

bronze_path = 'local_datalake/bronze/raw_data.json'
df_bronze = spark.read.option("multiline", "true").json(bronze_path)

df_silver = df_bronze.dropna()

silver_path = "local_datalake/silver/cleaned_data"
df_silver.write.mode('overwrite').parquet(silver_path)

print("all data cleaned and saved in silver in parquet")

spark.stop()