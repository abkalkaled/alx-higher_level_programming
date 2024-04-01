#!/usr/bin/python3
"""10 recent commits in repo"""
import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}"
    response = requests.get(url)

    if response.status_code == 200:
        repo_info = response.json()
        print("Repository name:", repo_info["name"])
        print("Owner:", repo_info["owner"]["login"])
        print("Description:", repo_info["description"])
        print("URL:", repo_info["html_url"])
        print("Language:", repo_info["language"])
        print("Stars:", repo_info["stargazers_count"])
    else:
        print("Failed to retrieve. Status code:", response.status_code)
