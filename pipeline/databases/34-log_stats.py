#!/usr/bin/env python3
"""Script that provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx

total = collection.count_documents({})

get = collection.count_documents({ "method": "GET"})
post = collection.count_documents({ "method": "POST"})
put = collection.count_documents({ "method": "PUT"})
patch = collection.count_documents({ "method": "PATCH"})
delete = collection.count_documents({ "method": "DELETE"})

status = collection.count_documents({"method": "GET", "path": "/status"})

print("{} logs".format(total))
print("Methods:")
print("\tmethod {}: {}".format("GET", get))
print("\tmethod {}: {}".format("POST", post))
print("\tmethod {}: {}".format("PUT", put))
print("\tmethod {}: {}".format("PATCH", patch))
print("\tmethod {}: {}".format("DELETE", delete))
print("{} status check".format(status))
