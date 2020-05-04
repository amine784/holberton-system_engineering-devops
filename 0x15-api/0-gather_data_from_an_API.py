#!/usr/bin/python3
from sys import argv
import requests as req
q = req.get("{}users/{}".format(
    "https://jsonplaceholder.typicode.com/", argv[1]))
query = req.get("{}todos".format(
    "https://jsonplaceholder.typicode.com/"), params={"userId": argv[1]})
q = q.json()
query = query.json()
n = q.get("name")
count = len(query)
done = 0
header = []
for dt in query:
    if dt.get("completed") is True:
        done += 1
        header.append(dt["title"])
print(f"Employee {n} is done with tasks {done}/{count}:")
for title in header:
    print("\t {}".format(title))
if __name__ == "__main__":
    pass
