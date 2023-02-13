import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    # Storage connection string (NOT recommended, used for simplicity for this study)
    conn_string = "REPLACE THIS"

    # Create the BlobServiceClient object and access the container
    blob_service_client = BlobServiceClient.from_connection_string(conn_string)
    container_name = "test-container"
    blob_to_access = "test2.txt"

    # test
    containers = blob_service_client.list_containers()
    for container in containers:
        print(container.name)
    
    # Using container name and BlobServiceClient, access a specific container via ContainerClient
    container_client = blob_service_client.get_container_client(container=container_name)

    # Print existing blob from storage container with BlockBlobClient
    blob_client = container_client.get_blob_client(blob=blob_to_access)
    print(blob_client.download_blob().readall())


except Exception as ex:
    print('Exception:')
    print(ex)