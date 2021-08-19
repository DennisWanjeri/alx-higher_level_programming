#!/bin/bash
# takes in an URL as an arguement, sends a GET requeat to the URL
# displays the body of the response
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
