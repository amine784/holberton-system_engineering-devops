#!/usr/bin/python3
"""python script"""
import csv
from sys import argv
import json
import requests as req
if __name__ == "__main__":
    q = req.get("{}users/{}".format(
        "https://jsonplaceholder.typicode.com/", argv[1]))
    query = req.get("{}todos".format(
        "https://jsonplaceholder.typicode.com/"), params={"userId": argv[1]})
    q = q.json()
    query = query.json()
    n = q.get("username")
    d = []
    for task in query:
        data = {}
        data['username'] = n,
        data['completed'] = task.get('completed'),
        data['task'] = task.get('title')
        d.append(data)
    with open("{}.json".format(argv[1]), "w", newline="") as json_f:
        json.dump({argv[1]: d}, json_f)
