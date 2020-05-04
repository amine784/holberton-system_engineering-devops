#!/usr/bin/python3
"""python script"""
from sys import argv
import json
import requests as req
if __name__ == "__main__":
    ret = {}
    title = "todo_all_employees.json"
    rs = req.get("{}users".format(
        "https://jsonplaceholder.typicode.com/"))
    rs = rs.json()
    for userid in rs:
        Id = userid.get("id")
        list = []
        t = req.get("{}todos".format(
                "https://jsonplaceholder.typicode.com/"),
                            params={"userId": Id})
        t = t.json()
        name = userid.get("username")
        for rep in t:
            dic = {}
            dic["username"] = name
            dic["task"] = rep.get("title")
            dic["completed"] = rep.get("completed")
            list.append(dic)
        ret[Id] = list
    with open(title, 'w') as jason:
        json.dump(ret, jason)
