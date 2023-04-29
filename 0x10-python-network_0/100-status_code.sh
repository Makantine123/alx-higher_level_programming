#!/bin/bash
# Script sends a request to a URL as an augument and displays the status code
curl -sLw "%{http_code}" -o /dev/null "$1"
