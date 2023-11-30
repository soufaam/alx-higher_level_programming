#!/bin/bash
#Display only body of a 200 status code response
curl -i -L -X OPTIONS "$1" | grep "Allow:"
