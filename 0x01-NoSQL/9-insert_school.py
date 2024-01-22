#!/usr/bin/env python3
"""manipulating MongoDBs with Pymongo"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document to mongo_collection"""
    return mongo_collection.insert(kwargs)
