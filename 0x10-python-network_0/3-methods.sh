#!/bin/bash
# list Options available!
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
