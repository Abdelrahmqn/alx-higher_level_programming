#!/bin/bash
# send a Post req, email header with value: test@gmail.com, .....etc
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
