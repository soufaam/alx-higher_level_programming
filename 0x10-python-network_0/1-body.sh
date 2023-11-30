#!/bin/bash
#Display only body of a 200 status code response
status=$(curl -s -w "%{http_code}"  -o /dev/null "$1")
if [ "$status" -eq 200 ]; then
curl -s "$1"
fi
