#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the
body of the response.
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    status = response.status_code

    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(response.text)
