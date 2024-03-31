#!/bin/bash
# sends request to URL and displays body size in bytes
curl -s "$1" | wc -c
