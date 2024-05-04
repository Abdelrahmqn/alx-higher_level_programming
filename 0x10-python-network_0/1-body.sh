#!/bin/bash
# send a GET reQ to the URL, and display body of response.
curl -s -w "%{http_code}" "$1" | grep -q "200" | echo -n "Route $(wc -c)"
