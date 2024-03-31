#!/bin/bash
# script that takes url and displays HTTP method
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
