#!/usr/bin/env python3
"""
This module have a utility function that list all document
"""
import pymongo


def list_all(mongo_collection):
    """list all collections"""
    if not mongo_collections:
        return []
    return list(mongo_collections.find())
