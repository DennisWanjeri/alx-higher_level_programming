#!/bin/bash
# sends request to a url, displays only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
