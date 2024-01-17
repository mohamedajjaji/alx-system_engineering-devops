#!/usr/bin/python3
"""
Function to print hot posts on a given Reddit subreddit """
import requests


def top_ten(subreddit):
    """ Print the titles of the 10 hottest posts on a given subreddit """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    try:
        if response.status_code != 200:
            print("None")
            return
        else:
            results = response.json().get("data")
            [print(c.get("data").get("title"))for c in results.get("children")]
    except ValueError as e:
        print("Error decoding JSON:", e)
        return 0
