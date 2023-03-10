import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


# Storage connection string (NOT recommended, used for simplicity for this study)
STORAGE_CONNECTION_STR = os.environ["STORAGE_CONNECTION_STR"]
STORAGE_CONTAINER_NAME = os.environ["STORAGE_CONTAINER_NAME"]
BLOB_NAME = "2022-12-22-09-00.txt"

# Sample code explaining the various client objects and some example methods
def download_blob():
    try:
        # Create the BlobServiceClient (client for a specific Azure Storage resource)
        blob_service_client = BlobServiceClient.from_connection_string(
            STORAGE_CONNECTION_STR
        )

        # Using container name and BlobServiceClient, access a specific container via ContainerClient (client for a specific container)
        container_client = blob_service_client.get_container_client(
            container=STORAGE_CONTAINER_NAME
        )

        # Print existing blob from storage container with BlobClient (client for a specific blob)
        blob_client = container_client.get_blob_client(blob=BLOB_NAME)
        print(blob_client.download_blob().readall())

    except Exception as ex:
        print("Exception:")
        print(ex)


# TODO: Using the Azure SDK reference documentation, complete the list_blobs_in_container() method.
# Hint: Note the relationship between BlobServiceClient, ContainerClient, and BlobClient.
def list_blobs_in_container():
    print("List of blobs in container:")
    try:
        pass

    except Exception as ex:
        print("Exception:")
        print(ex)


# Sample code
# download_blob()

# Problem to be executed by the participant
list_blobs_in_container()
