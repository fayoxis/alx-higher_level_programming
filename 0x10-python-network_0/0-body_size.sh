#!/bin/bash
# script that takes in a URL, sends a request to that URL
curl -s "$1" | wc -c
