#!/usr/bin/env python3
"""manipulating MongoDBs with Pymongo"""


def update_topics(mongo_collection, name, topics):
    """changes specifc topics to documents identified by their name"""
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)
