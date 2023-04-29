#!/usr/bin/python3
"""Script takes a URL, sends a request to URL and displays the value of the
X-Request-Id variable found in the header of the response"""

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header = response.info()
    x_request = header.get('X-Request-Id')

print(x_request)
