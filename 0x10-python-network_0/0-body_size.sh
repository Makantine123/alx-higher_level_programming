#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
response_size=$(curl -s -w '%(size_download)' -o /dev/null "$1")
echo "$response_size"
