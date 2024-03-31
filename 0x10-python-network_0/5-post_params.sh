#!/bin/bash
# shell script to send a post request and displays body of resonse"
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
