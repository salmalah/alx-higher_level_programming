#!/usr/bin/python3
"""
a script that takes in a URL sends a request to the URL and displays the body
"""
import sys
import urllib.request as ur
import urllib.error as ue

if __name__ == "__main__":
    u = sys.argv[1]
    try:
        with ur.urlopen(u) as re:
            content = re.read().decode('utf-8')
            print(content)
    except ue.HTTPError as e:
        print(f"Error code: {e.code}")
