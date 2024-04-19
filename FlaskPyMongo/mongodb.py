from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import random


# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://xabcd9172:xabcd9172@cluster0.euudrlp.mongodb.net/"
session = random.randint(0, 100)
# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    for i in range(30):

        json_data = {
            "session" : session,
            "name": "Sp02",
            "value": random.randint(0, 100),
            "timestamp": datetime.now()
        }
        client.data.parameters.insert_one(json_data)
    client.admin.command('ping')

    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

