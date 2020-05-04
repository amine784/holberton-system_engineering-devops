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
    count = len(query)
    done = 0
    header = []
    d = []
    with open("{}.json".format(argv[1]), "w", newline="") as json_f:
        dic = {}
        for dt in query:
            dic['username'] = q.get("username")
            dic['complited'] = dt.get('completed')
            dic['task'] = dt.get('title')
            d.append(dic)
        json.dump({argv[1]: d}, json_f)
