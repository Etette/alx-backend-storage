#!/usr/bin/env python3
"""
Write a Python script that provides some stats about
Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def nginx_stats_check():
    """ provides some stats about Nginx logs
    stored in MongoDB"""
    client = MongoClient()
    collect_nginx = client.logs.nginx

    num_of_docs = collect_nginx.count_documents({})
    print("{} logs".format(num_of_docs))
    print("Methods:")

    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods_list:
        method_count = collect_nginx.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))
    status = collect_nginx.count_documents({"method": "GET",
                                           "path": "/status"})
    print("{} status check".format(status))


if __name__ == "__main__":
    nginx_stats_check()
