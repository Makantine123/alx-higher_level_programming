#!/usr/bin/python3
"""
Scripts uses github api to fetch commits from a repo
"""

import requests
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        password, username)

    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
