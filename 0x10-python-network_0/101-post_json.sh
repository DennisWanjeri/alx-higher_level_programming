#!/bin/bash
# sends a JSON POST request to a url
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
