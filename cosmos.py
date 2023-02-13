import os
import json

from azure.cosmos import CosmosClient, PartitionKey

ENDPOINT = os.environ['ENDPOINT']
KEY = os.environ['KEY']

DATABASE_NAME = os.environ['DATABASE_NAME']
CONTAINER_NAME = os.environ['CONTAINER_NAME']

# Sample code that upserts (updates or inserts) data  in the CosmosDB.
def upsertItem(id: str, partitionKey: int):
    client = CosmosClient(url=ENDPOINT, credential=KEY)
    database = client.get_database_client(DATABASE_NAME)
    container = database.get_container_client(CONTAINER_NAME)

    item = container.read_item(id, partition_key=partitionKey)

    # item updates go here

    # upsert item
    existing_item = container.upsert_item(item)

# TODO: Using the Azure SDK reference documentation, complete the query() method.
# Use the SDK to query the following command on the database: 
# SELECT * FROM collection c WHERE c.Elevation = <input-param-from-func> ORDER BY c.Country ASC OFFSET 0 LIMIT <input-param-from-func>
# Hint: You can re-use the code to create your clients to interact with the CosmosDB.
def query_by_elevation(elevation: int, limit: int):
    query = "SELECT * FROM collection c LIMIT 5"
    pass

upsertItem()
query_by_elevation()