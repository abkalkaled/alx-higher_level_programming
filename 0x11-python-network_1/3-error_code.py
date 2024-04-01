#!/usr/bin/python3
""" handles httpError"""
import sys
import urllib.request
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except HTTPError as e:
        print("Error code:", e.code)
