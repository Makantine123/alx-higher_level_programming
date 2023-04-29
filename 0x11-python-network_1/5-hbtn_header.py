#!/usr/bin/python3
"""
Python scriot fetches https://alx-intranet.hbtn.io/status
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
