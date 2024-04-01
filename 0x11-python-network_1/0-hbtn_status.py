#!/usr/bin/python3
""" Python script that fetch https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    html = response.read().decode('utf-8')

print("Body response:")
print("\t- type:", type(html))
print("\t- content:", html)
