#!/usr/bin/python3
"""
Script that takes Github credentials (username and password)
and uses the GitHub API to display id
"""

import requests
import sys

from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]

    auth = HTTPBasicAuth(username, password)

    response = requests.get(
        "https://api.github.com/users", auth=auth)

    if response.ok:
        data = response.json()
        print(data.get('id'))
    else:
        print('None')
