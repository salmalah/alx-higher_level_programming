#!/bin/bash
# a Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -sw -X POST -H "User-Agent: You got me!" 0.0.0.0:5000/catch_me
