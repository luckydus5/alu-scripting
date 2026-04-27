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
    headers = {"User-Agent": "linux:alu.scripting:v1.0 (by /u/alu)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print("None")
