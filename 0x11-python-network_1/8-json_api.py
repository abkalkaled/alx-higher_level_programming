#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    response = requests.post(url, data=data)

    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result['id'], result['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
