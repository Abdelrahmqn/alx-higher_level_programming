#!/bin/bash
# checking the length of the url
curl -s "$1" | wc -c
