#!/bin/bash
#Bash script that takes URL, sends a request and displays size of the body of response
curl -sI "$1" | grep Content-Length | awk -F' ' '{print $2}'
