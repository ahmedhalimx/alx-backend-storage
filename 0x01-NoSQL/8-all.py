#!/usr/bin/env python3
"""manipulating MongoDBs with Pymongo"""


def list_all(mongo_collection):
    """ list all documents"""
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
