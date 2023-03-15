#!/usr/bin/python3
"""A Python script that fetches the intranet status page using the requests package"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)

    # Raise an exception for any status code that is not a success
    response.raise_for_status()

    # Display the body of the response in the specified format
    data = response.json()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))