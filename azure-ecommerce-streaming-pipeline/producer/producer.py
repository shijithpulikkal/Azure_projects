"""
producer.py — Simulates a live stream of e-commerce order events
and sends them to Azure Event Hubs.
"""

import asyncio
import json
import random
import os
from datetime import datetime, timezone
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

CONNECTION_STR = os.environ["EVENTHUB_CONNECTION_STRING"]
EVENTHUB_NAME = "eh-order-events"

PRODUCT_CATEGORIES = [
    "electronics", "home_appliances", "fashion", "books",
    "sports", "toys", "beauty", "furniture"
]
STATES = ["SP", "RJ", "MG", "RS", "PR", "BA", "SC", "PE"]


def generate_event() -> dict:
    return {
        "order_id": f"ord-{random.randint(100000, 999999)}",
        "customer_state": random.choice(STATES),
        "product_category": random.choice(PRODUCT_CATEGORIES),
        "quantity": random.randint(1, 5),
        "unit_price": round(random.uniform(10, 500), 2),
        "event_time": datetime.now(timezone.utc).isoformat(),
    }


async def run():
    producer = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STR, eventhub_name=EVENTHUB_NAME
    )
    async with producer:
        print("Streaming simulated order events... Ctrl+C to stop.")
        while True:
            batch = await producer.create_batch()
            event = generate_event()
            batch.add(EventData(json.dumps(event)))
            await producer.send_batch(batch)
            print(f"Sent: {event}")
            await asyncio.sleep(random.uniform(0.5, 2))  # simulate irregular order timing


if __name__ == "__main__":
    asyncio.run(run())