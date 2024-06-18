#!/usr/bin/env python3
"""
Using pymongo to modify documents
"""


def update_topics(mongo_collection, name, topics):
    """
    This function changes all topics of a school docoument based on the name
    """
    mongo_collection.update_many({"name": name}, {$set:{"topic": topics}})
