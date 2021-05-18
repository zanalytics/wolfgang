import logging
import os
import pandas as pd
from datetime import datetime
from azure.storage.blob import BlobServiceClient

#set time
dateTime = datetime.now()
timestamp = dateTime.strftime("%d-%b-%Y_%H:%M:%S")

#output container
fileName= f"stockmarket_{timestamp}.csv"
containerName = "stockmarket"

def main(df: str):
    data = pd.read_json(df)
    output = data.to_csv(encoding = "utf-8")

    connection_string= os.environ['ConnectionString']
    # Instantiate a new BlobServiceClient using a connection string
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    # Instantiate a new ContainerClient
    container_client = blob_service_client.get_container_client(containerName)

    # Instantiate a new BlobClient
    blob_client = container_client.get_blob_client(fileName)
    # upload data
    blob_client.upload_blob(output, blob_type="BlockBlob")

    return f"Data sent to Blob"