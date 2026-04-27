#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "python:api_advanced_0:v1.0.0 (by /u/johndoe_123)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    return 0
