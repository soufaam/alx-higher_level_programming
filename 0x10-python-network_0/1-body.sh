#!/bin/bash
#Display only body of a 200 status code response
res=$(curl -s -LI "$1" -o /dev/null -w '%{http_code}')
if [ "$res" == "200" ]; then curl -s "$1"; fi
