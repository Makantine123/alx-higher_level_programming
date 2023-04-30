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

    auth_headers = {
        "Authorization": "Base {}:{}".format(username, password)
    }

    response = requests.get(
        "https://api.github.com/user", headers=auth_headers)

    if response.ok:
        data = response.json()
        print(data.get('id'))
    else:
        print('None')
