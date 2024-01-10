#!/bin/bash
# Sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response. It sends a `POST` request with the contents of a file, passed with the filename as the second argument, in the body of the request.
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
