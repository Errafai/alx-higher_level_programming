#!/bin/bash
curl -s -w "%{size_download}\n" -o /dev/null $1
