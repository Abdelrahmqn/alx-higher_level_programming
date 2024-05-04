#!/bin/bash
# list Options available!
curl -sI OPTIONS "$1 | grep "Allow" | cut -d " " -f 2-
