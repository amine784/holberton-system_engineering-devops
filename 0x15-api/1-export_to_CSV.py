#!/usr/bin/python3
import csv
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
with open(f"{argv[1]}.csv", "w", newline="") as csv_f:
    writer = csv.writer(csv_f, quoting=csv.QUOTE_ALL)
    for dt in query:
        writer.writerow([argv[1], n, dt.get("completed"),
                         dt.get('title')])
if __name__ == "__main__":
    pass
