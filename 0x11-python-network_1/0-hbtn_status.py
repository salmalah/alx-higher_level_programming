#!/usr/bin/python3
"""
a script that fetches https://alx-intranet.hbtn.io/status using urllib
"""
import urllib.request


if __name__ == "__main__":
    u = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(u) as r:
        info = r.read()
        print("Body response:")
        print("\t- type:", type(info))
        print("\t- content:", info)
        print("\t- utf8 content:", info.decode('utf-8'))
