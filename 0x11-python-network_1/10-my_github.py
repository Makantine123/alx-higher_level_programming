#!/usr/bin/python3
"""
Script that takes Github credentials (username and password)
and uses the GitHub API to display id
"""

import requests
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(
        "https://api.github.com/user", auth=(username, password))

    if response.ok:
        data = response.json()
        print(data.get('id'))
    else:
        print('None')
