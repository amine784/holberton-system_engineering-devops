#!/usr/bin/python3
from sys import argv
import csv
import requests as req
if __name__ == "__main__":
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
    with open("{}.csv".format(argv[1]), "w", newline="") as csv_f:
        data = csv.writer(csv_f, quoting=csv.QUOTE_ALL)
        for dt in query:
            data.writerow([argv[1], n, dt.get("completed"), dt.get('title')])
