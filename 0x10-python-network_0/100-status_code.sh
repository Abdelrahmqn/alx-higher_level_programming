#!/bin/bash
#req, display status.
curl -o /dev/null --silent --head --write-out '%{http_code}' "$1"
