#!/bin/bash
#get the the allowed method in the web server
curl -sI -X OPTIONS $1
