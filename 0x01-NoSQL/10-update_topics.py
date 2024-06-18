#!/usr/bin/env python3
"""
Using pymongo to modify documents
"""


def update_topics(mongo_collection, name, topic):
    """
    This function changes all topics of a school docoument based on the name
    """
    mongo_collection.update({name: name}, {$set:{topic}})
