#!/usr/bin/python3
"""A Python script that sends a request to a URL and displays the value of the X-Request-Id header"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    # Display the value of the X-Request-Id header if it exists
    if "X-Request-Id" in response.headers:
        print(response.headers["X-Request-Id"])
