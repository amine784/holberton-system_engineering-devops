#!/usr/bin/python3
'''python script'''
import requests


def top_ten(subreddit):
    '''function to check nbre of sub'''
    requestpost = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit), headers={"User-Agent": "amine"})
    if requestpost.status_code == 404:
        print("None")
    else:
        response_data = requestpost.json()
        for data in response_data["data"]["children"][:10]:
            print(data["data"]["title"])
