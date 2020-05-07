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
    st = request_data["data"]["after"]
    child = request_data["data"]["children"]
    for c in child:
        hot_list.append(c["data"]["title"])
    if st is not None:
        recurse(subreddit, hot_list, st)
    return(hot_list)
