#!/bin/bash
#cURL body size
curl -s -w "%{size_download}"  -o /dev/null $1
