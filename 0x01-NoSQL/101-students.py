#!/usr/binenv python3
"""
Write a Python function that returns all students
sorted by average score
"""


def top_students(mongo_collection):
    """ students by score """
    return mongo_collection.aggregate([
        {
            "$projects":
            {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
                }
            },
        {
            "$sort":
            {
                "averageScore": -1
                }
            }
        ])
