#!/usr/bin/python3
"""python script"""
from sys import argv
import json
import requests as req
if __name__ == "__main__":
    title = "todo_all_employees.json"
    q = req.get("{}users".format(
        "https://jsonplaceholder.typicode.com/"))
    q = q.json()
    d = []
    for data in q:
        Id = data.get('id')
        query = req.get("{}todos".format(
            "https://jsonplaceholder.typicode.com/"),
                        params={"userId": Id})
        query = query.json()
        n = data.get("username")
        for r in query:
            z = {}
            z['task'] = r.get('title')
            z['completed'] = r.get('completed')
            z['username'] = n
            d.append(z)
        with open(title, "w") as json_f:
            json.dump({Id: d}, json_f)
