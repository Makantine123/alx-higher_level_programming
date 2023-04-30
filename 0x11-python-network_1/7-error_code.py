#!/usr/bin/python3
"""
Script takes URL, sends request to the URL, displays the body of the response
"""

import requests
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    response = requests.get(url)
    try:
        print(response.text)
    except Exception:
        print(response.status_code)
