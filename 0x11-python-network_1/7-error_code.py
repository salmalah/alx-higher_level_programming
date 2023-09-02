#!/usr/bin/python3
"""
a script that takes in a URL sends a request to the URL and displays the body
"""
import sys
import requests as r


if __name__ == "__main__":
    u = sys.argv[1]
    try:
        re = r.get(u)
        re.raise_for_status()
        content = re.text
        print(content)
    except r.exceptions.HTTPError as m:
        print(f"Error code: {m.response.status_code}")
