#!/bin/bash 
#this  script that sends a request to a URL passed as an argument
curl -s -L -X HEAD -w "%{http_code}" "$1"
