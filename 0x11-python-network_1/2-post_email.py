#!/usr/bin/python3
""" script that sends post request to url with email"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    try:
        with urllib.request.urlopen(url, data=data) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        print("Error:", e.reason)
