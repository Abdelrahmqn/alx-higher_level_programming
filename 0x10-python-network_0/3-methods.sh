#!/bin/bash
# list Options available!
curl -sL OPTIONS "$1 | grep "Allow" | cut -d " " -f 2-
