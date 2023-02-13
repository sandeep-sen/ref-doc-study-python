import os
import json
import datetime

from azure.cosmos import CosmosClient, PartitionKey

ENDPOINT = os.environ["ENDPOINT"]
KEY = os.environ["KEY"]

DATABASE_NAME = os.environ["DATABASE_NAME"]
CONTAINER_NAME = os.environ["CONTAINER_NAME"]

# Sample code that upserts (updates or inserts) data  in the CosmosDB.


def upsertItem(id: str, partitionKey: int):
    client = CosmosClient(url=ENDPOINT, credential=KEY)
    database = client.get_database_client(DATABASE_NAME)
    container = database.get_container_client(CONTAINER_NAME)

    item = container.read_item(id, partition_key=partitionKey)
    date_string = datetime.datetime.now().isoformat()
    item["Region"] = f"Chile-S ({date_string})"
    response = container.upsert_item(body=item)
    print("Upserted Item's \n{0}".format(json.dumps(response, indent=True)))


# TODO: Using the Azure SDK reference documentation, complete the query() method.
# Use the SDK to query the following command on the database:
# SELECT * FROM collection c WHERE c.Elevation = <input-param-from-func> ORDER BY c.Country ASC OFFSET 0 LIMIT <input-param-from-func>
# Hint: You can re-use the code to create your clients to interact with the CosmosDB.


def query_by_elevation(elevation: int, limit: int):
    client = CosmosClient(url=ENDPOINT, credential=KEY)
    database = client.get_database_client(DATABASE_NAME)
    container = database.get_container_client(CONTAINER_NAME)

    query_string = "SELECT * FROM collection c WHERE c.Elevation = @elevation ORDER BY c.Country ASC OFFSET 0 LIMIT @limit"
    params = [
        dict(name="@elevation", value=elevation),
        dict(name="@limit", value=limit),
    ]

    results = container.query_items(
        query=query_string, parameters=params, enable_cross_partition_query=False
    )
    items = [item for item in results]
    output = json.dumps(items, indent=True)
    print("Result list\t", output)


upsertItem("7408d446-fb51-e70e-9955-560a0c966b68", 0)
query_by_elevation(0, 5)
