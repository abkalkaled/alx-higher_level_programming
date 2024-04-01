#!/usr/bin/python3
"""lists the 10 most recent commits on repo"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    repo = requests.get(url)
    commits = repo.json()
    try:
        for r in range(10):
            print("{}: {}".format(
                commits[r].get("sha"),
                commits[r].get("commit").get("author").get("name")))
    except IndexError:
        pass
