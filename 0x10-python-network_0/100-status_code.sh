#!/bin/bash
# script to return the request status code
curl -s -o /dev/null -w "%{http_code}" "$1"
