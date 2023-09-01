#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
"""
import urllib.request
import sys as s

if __name__ == "__main__":
    u = s.argv[1]
    with urllib.request.urlopen(u) as re:
        h = re.info()
        x_r_id = h.get('X-Request-Id')
    if x_r_id:
        print(x_r_id)
