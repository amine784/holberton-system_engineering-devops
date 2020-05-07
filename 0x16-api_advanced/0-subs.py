#!/usr/bin/python3
'''python script'''
import requests


def number_of_subscribers(subreddit):
    '''function to check nbre of sub'''
    headers = {"User-Agent": "amine"}
    requestpost = requests.get("https://www.reddit.com/r/{}/about.json".format(
        subreddit), headers=headers)
    if requestpost.status_code == 404:
        return (0)
    else:
        response_data = requestpost.json()
        return(response_data["data"]["subscribers"])
