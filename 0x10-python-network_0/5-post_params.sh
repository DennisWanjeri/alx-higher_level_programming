#!/bin/bash
# takes in a url sends a POST request to the passed URL, displays its body
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
