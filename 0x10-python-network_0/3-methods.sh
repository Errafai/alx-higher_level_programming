#!/bin/bash
#get the the allowed method in the web server
curl -sI $1 | grep "Allow" | cut -d " " -f 2-
