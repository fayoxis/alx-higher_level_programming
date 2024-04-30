#!/bin/bash
# this script that sends a DELETE request to the URL passed as argument
curl -s "$1" -X DELETE
