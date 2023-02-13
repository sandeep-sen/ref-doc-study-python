import asyncio

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient, EventHubConsumerClient

# Event Hubs connection string (NOT recommended, used for simplicity for this study)
EVENT_HUB_CONNECTION_STR = "REPLACE_THIS"
EVENT_HUB_NAME = "python-eh"

async def send_messages():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME
    )
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData("1"))
        event_data_batch.add(EventData("2"))
        event_data_batch.add(EventData("3"))
        event_data_batch.add(EventData("4"))
        event_data_batch.add(EventData("5"))
        event_data_batch.add(EventData("6"))
        event_data_batch.add(EventData("7"))
        event_data_batch.add(EventData("8"))
        event_data_batch.add(EventData("9"))
        event_data_batch.add(EventData("10"))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

        # Now that you've sent messages, receive them from the Event Hub.
        recv_messages()

# Method to handle incoming events
async def on_event(partition_context, event):
    print("Received event: {} from partition: {}.".format(event.body_as_str(), partition_context.partition_id))
    await partition_context.update_checkpoint(event)


# TODO: Using the Azure SDK reference documentation, complete the recv_messages() method.
# Hints:
# 1. Just like the producer code, you will need to create a client to asynchronously consume events from the Event Hub.
# 2. When creating a client to consume events, set the parameter 'consumer_group' to "$Default"
# 3. When creating a client to consume events, there is an 'on_event' parameter where you can pass in a method to handle incoming events.
async def recv_messages():
    consumer = EventHubConsumerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME, consumer_group="$Default",
    )
    async with consumer:
        await consumer.receive(
               starting_position="-1",  # "-1" is from the beginning of the partition.
               on_event=on_event
        )


#asyncio.run(send_messages())
asyncio.run(recv_messages())