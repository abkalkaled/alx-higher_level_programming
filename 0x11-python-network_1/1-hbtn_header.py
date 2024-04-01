#!/usr/bin/python3
"""A script that displays value of request-Id"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        x_request_id = response.headers.get("X-Requesr-Id")
        print(x_request_id)
