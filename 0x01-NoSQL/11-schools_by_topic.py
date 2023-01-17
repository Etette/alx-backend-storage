#!/usr/bin/env python3
"""
Write a Python function that returns the list of school having
a specific topic
"""
import pymongo


def schools_by_toopic(mongo_collection, topic):
    """Find by topic"""
    return mongo_collection.find({"topics": topic})
