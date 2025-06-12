#!/bin/bash
#get the html body of a website in $1 and count its length
curl -s $1 | wc -m
