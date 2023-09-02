#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
"""
import requests as r
import sys as s

if __name__ == "__main__":
    u = s.argv[1]
    re = r.get(u)
    x_r_id = re.headers.get('X-Request-Id')
    if x_r_id:
        print(x_r_id)
