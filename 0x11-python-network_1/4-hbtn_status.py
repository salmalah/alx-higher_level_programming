#!/usr/bin/python3
"""
a script that fetches https://alx-intranet.hbtn.io/status using requests
"""
import requests as r


if __name__ == "__main__":
    u = "https://alx-intranet.hbtn.io/status"
    re = r.get(u)
    i = re.text
    print("Body response:")
    print("\t- type:", type(i))
    print("\t- content:", i)
