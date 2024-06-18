#!/usr/bin/env python3
"""
This module inserts a new document in a collection using Python
"""


def insert_school(mongo_collection, **kwargs):
    """
    This function inserts a new document in a collection based on kwwargs
    """
    return mongo_collection.insert(kwargs)
