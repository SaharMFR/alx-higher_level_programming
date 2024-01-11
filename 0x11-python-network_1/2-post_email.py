#!/usr/bin/python3
"""
Takes in a URL and an email, sends a `POST` request to the passed URL
with the email as a parameter, and displays the body of the response.
(decoded in `utf-8`)
"""

import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    record = {"email": sys.argv[2]}
    formatted = urllib.parse.urlencode(record).encode("ascii")
    request = urllib.request.Request(sys.argv[1], formatted)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
