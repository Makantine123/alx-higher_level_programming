#!/usr/bin/python3
"""
Script takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, display the body of response
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    response = requests.post(url, data)
    print(response.text)
