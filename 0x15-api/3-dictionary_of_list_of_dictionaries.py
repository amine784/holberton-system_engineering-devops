#!/usr/bin/python3
"""python script"""
from sys import argv
import json
import requests as req
from requests import get
if __name__ == "__main__":
    title = "todo_all_employees.json"
    data = {}
    url = "https://jsonplaceholder.typicode.com/"
    users = get(url + "users").json()
    for user in users:
        Id = user.get("id")
        list = []
        tasks = get(url + "todos?userId={}".format(Id)).json()
        for rep in tasks:
            dic = {}
            dic["username"] = user.get("username")
            dic["task"] = rep.get("title")
            dic["completed"] = rep.get("completed")
            list.append(dic)
        data[Id] = list
    with open(title, 'w') as json_file:
        json.dump(data, json_file)
