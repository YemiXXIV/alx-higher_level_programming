#!/bin/bash
# Bash script thst takes URL, sneds a POST request and displays body of response
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
