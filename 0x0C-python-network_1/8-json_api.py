#!/usr/bin/python3
"""Script that takes a letter and sends a POST request to http://0.0.0.0:5000/search_user"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    try:
        url = 'http://0.0.0.0:5000/search_user'
        data = {'q': q}
        response = requests.post(url, data=data)

        if response.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.json().get('id'), response.json().get('name')))
    except ValueError:
        print("Not a valid JSON")
    except:
        print("Error: Could not connect to server")
