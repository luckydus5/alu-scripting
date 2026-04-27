#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Queries the Reddit API recursively and returns the list of hot articles.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.scripting:v1.0 (by /u/alu)"}
    params = {"after": after, "limit": 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))

        after = data.get("data", {}).get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
