#!/bin/bash
#cURL body size
curl -s -w "%{size_download}\n"  -o /dev/null 127.0.0.1:5000
