#!/usr/bin/env python3
"""manipulating MongoDBs with Pymongo"""


def schools_by_topic(mongo_collection, topic):
    """returns a list of school documents with specific topic"""
    documents = mongo_collection.find({"topics": topic})
    return list(documents)
