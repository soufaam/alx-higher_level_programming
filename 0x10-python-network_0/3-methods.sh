#!/bin/bash
#Display only body of a 200 status code response
curl -I $1 2>/dev/null | awk '/Allow:/ {print substr($0, index($0,$2))}'
