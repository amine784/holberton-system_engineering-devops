#!/usr/bin/python3
'''python script'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''function to check nbre of sub'''
    requestpost = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit), headers={"User-Agent": "amine"}, params={"after": after})
    if requestpost.status_code != 200:
        return(None)
    request_data = requestpost.json()
    for c in request_data["data"]["children"]:
        hot_list.append(c["data"]["title"])
    st = request_data["data"]["after"]
    if st is not None:
        recurse(subreddit, hot_list, st)
    return(hot_list)
