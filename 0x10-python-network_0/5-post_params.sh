#!/bin/bash
#Display only body of a 200 status code response
curl -d  "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1" 2>/dev/null
