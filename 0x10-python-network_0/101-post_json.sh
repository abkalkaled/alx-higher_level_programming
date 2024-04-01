#!/bin/bash
# JSON POST request to a given URL with a server
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
