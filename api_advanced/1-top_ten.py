#!/usr/bin/python3
"""
Function that queries the Reddit API and prints titles the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API to print the first 10 hot posts
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:api_advanced_1:v1.0.0 (by /u/johndoe_123)"
    }
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if not posts:
            print(None)
            return
        for post in posts[0:10]:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
