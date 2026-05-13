import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()

connection_string = os.getenv("AZURE_CONNECTION")

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

bronze_container = "bronze-layer"

container_client = blob_service_client.get_container_client(bronze_container)

if not container_client.exists():
    container_client.create_container()
    print("it was created")

blob_client = container_client.get_blob_client(blob="raw_data.json")

with open("raw_data.json", "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
    print("succesfully added")