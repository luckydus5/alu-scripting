#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after="", word_count={}):
    """
    Queries the Reddit API recursively and counts the occurrences
    of given keywords in the titles of hot articles.
    """
    if not word_count:
        for word in word_list:
            if word.lower() not in word_count:
                word_count[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.scripting:v1.0 (by /u/alu)"}
    params = {"after": after, "limit": 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            title = post.get("data", {}).get("title").lower().split()
            for word in word_count.keys():
                word_count[word] += title.count(word)

        after = data.get("data", {}).get("after")
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_words = sorted(word_count.items(),
                                  key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_words:
                if count > 0:
                    print("{}: {}".format(word, count))
    else:
        pass
