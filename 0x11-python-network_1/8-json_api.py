#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
"""
import requests as r
import sys as s


if __name__ == "__main__":
    u = "http://0.0.0.0:5000/search_user"
    q = "" if len(s.argv) == 1 else s.argv[1]
    try:
        re = r.post(u, data={'q': q})
        data = re.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
