import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

from ..core.config import settings

try:
    print("Azure Blob Storage Python quickstart sample")

    account_url = settings.AZURE_BLOB_URL
    default_credential = DefaultAzureCredential()



except Exception as ex:
    print('Exception:')
    print(ex)

class AzureStorage:
    def __init__(self, container_name:str, local_file_name:str, upload_file_path:str):
        self.upload_file_path = upload_file_path
        self.blob_service_client = BlobServiceClient(account_url, credential=default_credential)

        self.container_client = self.blob_service_client.create_container(container_name)

        self.blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    def upload(self):
        with open(file=self.upload_file_path, mode="rb") as data:
            self.blob_client.upload_blob(data)

    def fetch(self, id):
