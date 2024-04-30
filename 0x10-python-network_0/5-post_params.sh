#!/bin/bash
# this send a POST request to the passed URL using curl
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
