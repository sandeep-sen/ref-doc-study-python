from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Storage connection string (NOT recommended, used for simplicity for this study)
STORAGE_CONNECTION_STR = "REPLACE_THIS"

# Sample code explaining the various client objects and some example methods
def download_blob():
    try:
        # Create the BlobServiceClient (client for a specific Azure Storage resource)
        blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STR)
        container_name = "test-container"
        blob_to_access = "test2.txt"
        
        # Using container name and BlobServiceClient, access a specific container via ContainerClient (client for a specific container)
        container_client = blob_service_client.get_container_client(container=container_name)

        # Print existing blob from storage container with BlobClient (client for a specific blob)
        blob_client = container_client.get_blob_client(blob=blob_to_access)
        print(blob_client.download_blob().readall())

    except Exception as ex:
        print('Exception:')
        print(ex)


# TODO: Using the Azure SDK reference documentation, complete the list_blobs_in_container() method.
# Hint: Note the relationship between BlobServiceClient, ContainerClient, and BlobClient.
def list_blobs_in_container():
    try:
        blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STR)
        container_name = "test-container"
        blob_to_access = "test2.txt"
        container_client = blob_service_client.get_container_client(container=container_name)
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            print(blob.name)

    except Exception as ex:
        print('Exception:')
        print(ex)

# Code to be executed
print("Trying to list blobs in container:")
list_blobs_in_container()