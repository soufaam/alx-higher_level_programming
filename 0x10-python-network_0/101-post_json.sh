#!/bin/bash
#Display only body of a 200 status code response
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"
