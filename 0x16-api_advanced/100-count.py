#!/usr/bin/python3
'''python script'''
import requests


def count_words(subreddit, word_list):
    '''function to check nbre of sub'''
    requestpost = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit), headers={"User-Agent": "amine"})
    if requestpost.status_code != 200:
        return(None)
    request_data = requestpost.json()
