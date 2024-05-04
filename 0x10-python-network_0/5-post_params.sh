#!/bin/bash
# send a Post req, email header with value: test@gmail.com, .....etc
curl -s -X POST -H "email: test@gmail.com" -H "subject: I will always be here for PLD" "$1"
