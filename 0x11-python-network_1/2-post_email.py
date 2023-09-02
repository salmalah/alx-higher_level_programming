#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request
"""
import urllib.parse as up
import urllib.request as ur
import sys as s


if __name__ == "__main__":
    u = s.argv[1]
    e = s.argv[2]
    d = up.urlencode({'email': e}).encode('ascii')
    req = ur.Request(u, d)
    with ur.urlopen(req) as re:
        content = re.read().decode('utf-8')
        print(content)
