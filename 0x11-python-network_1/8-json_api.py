#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to http://0.0.0.0:5000/
search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":

    if sys.argv[1]:
        q = sys.argv[1]
    else:
        q = ""

    data = {'q': q}
    url = 'http://0.0.0.0:500/search_user'

    response = requests.post(url, data)

    if response.ok:
        try:
            json_data = response.json()
            if len(json_data):
                print("No result")
            else:
                print("[{}] {}".format(json_data.get('id'),
                                       json_data.get('name')))
        except ValueError:
            print("Not a valid JSON")
    else:
        print("Error code: {}".format(response.status_code))
