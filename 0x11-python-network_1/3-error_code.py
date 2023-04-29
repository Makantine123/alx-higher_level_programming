#!/usr/bin/python3
"""
Script take in URL, sends a request to URL and displays the body of the
response (decoded in utf-8)
"""

import urllib.error
import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('UTF-8')
            print(data)
    except urllib.error.HTTPError as err:
        print("Error code: {}", err.code)
