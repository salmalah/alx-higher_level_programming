#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request
"""
import requests as r
import sys as s


if __name__ == "__main__":
    u = s.argv[1]
    e = s.argv[2]
    d = {'email': e}
    res = r.post(u, d)
    content = res.text
    print(content)
