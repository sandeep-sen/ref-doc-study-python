import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    # URL to storage account
    account_url = "https://stoaccsandeep.blob.core.windows.net"

    # Storage connection string (NOT recommended, used for simplicity for this study)
    conn_string = os.environ["AZURE_STORAGE_CONNECTION_STRING"]

    # Create the BlobServiceClient object and access the container
    blob_service_client = BlobServiceClient.from_connection_string(conn_string)
    container_name = "test-container"
    blob_to_access = "test.txt"
    
    # Using container name and BlobServiceClient, access a specific container via ContainerClient
    container_client = blob_service_client.get_container_client(container=container_name) 

    # Download existing blob from storage container
    local_path = "./data"
    download_file_path = os.path.join(local_path, str.replace(blob_to_access,'.txt', 'DOWNLOAD.txt'))
    print("\nDownloading blob to \n\t" + download_file_path)

    # Download the specific blob in the container
    with open(file=download_file_path, mode="wb") as download_file:
        download_file.write(container_client.download_blob(blob_to_access).readall())


except Exception as ex:
    print('Exception:')
    print(ex)