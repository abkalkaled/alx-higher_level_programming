#!/bin/bash
# script that request to 0.0.0.0:5000/catch_me that causes the server to respond
curl -sL -d "You got me!" "0.0.0.0:5000/catch_me"
