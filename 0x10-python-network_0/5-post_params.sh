#!/bin/bash
# Takes in a URL, sends a POST request to the passed URL, and displays the body of the response. A variable `email` must be sent with the value `test@gmail.com`, and a variable `subject` must be sent with the value `I will always be here PLD'.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here PLD" "$1"
