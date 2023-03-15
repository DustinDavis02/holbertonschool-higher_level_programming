#!/usr/bin/python3
"""This script takes in a URL and sends a request to display the value of request id value."""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.info().get('X-Request-Id'))