#!/usr/bin/python3
"""
A Python script that uses the GitHub API to display your GitHub user id.
"""
import requests as r
import sys as s

if __name__ == "__main__":
    username = s.argv[1]
    personal_at = s.argv[2]
    u = f"https://api.github.com/user"
    auth = (username, personal_at)
    res = r.get(u, auth=auth)
    print(res.json().get("id"))
