#!/usr/bin/python3
"""
A Python script that lists 10 commits from a specified
repository by a specified owner using the GitHub API.
"""
import requests as r
import sys as s

if __name__ == "__main__":
    r_name = s.argv[1]
    o_name = s.argv[2]
    u = f"https://api.github.com/repos/{o_name}/{r_name}/commits"
    try:
        res = r.get(u)
        res.raise_for_status()
        comts = res.json()[:10]
        for c in comts:
            sha = c.get('sha')
            au_name = c.get('commit').get('author').get('name')
            print(f"{sha}: {au_name}")
    except r.exceptions.RequestException as x:
        print(f"Error: {x}")
        sys.exit(1)
