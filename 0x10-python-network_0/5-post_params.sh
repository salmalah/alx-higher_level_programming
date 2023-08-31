#!/bin/bash
# Bash scripts that sends a POST request to the passed URL
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
