#!/usr/bin/env python3
"""
Using pymongo to carry out operations in mongodb
"""


def schools_by_topic(mongo_collection, topic):
    """
    This function finds and returns  schools that have a specific topic
    """
    documents = mongo_collection.find({"topic": topic})
    return list(document)
