from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import random
import matplotlib.pyplot as plt

# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://xabcd9172:xabcd9172@cluster0.euudrlp.mongodb.net/"

# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))

latest_data = client.db.test_database.find_one({}, sort=[("time", -1)])
print(latest_data)

session_data = client.data.parameters.find({"session": 35})

    # Extract timestamps and values from the documents
timestamps = []
values = []
for data in session_data:
    timestamps.append(data["timestamp"])
    values.append(data["value"])

    # Plot timestamp vs value graph
plt.plot(timestamps, values)
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Timestamp vs Value for Session: ' + "35")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()