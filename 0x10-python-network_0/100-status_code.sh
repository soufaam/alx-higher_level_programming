#!/bin/bash
#Display only body of a 200 status code response
curl -s -LI "$1" -o /dev/null -w '%{http_code}'

