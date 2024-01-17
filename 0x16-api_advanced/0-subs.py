#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit subreddit """
import requests


def number_of_subscribers(subreddit):
    """ Return the total number of subscribers on a given subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        if response.status_code != 200:
            print("Error: status code {}".format(response.status_code))
            return 0
        else:
            results = response.json().get("data")
            return results.get("subscribers")
    except ValueError as e:
        print("Error decoding JSON:", e)
        return 0
