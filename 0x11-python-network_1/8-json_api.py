#!/usr/bin/python3
"""
Takes in a letter and sends a `POST` request to
`http://0.0.0.0:5000/search_user` with the letter
as a parameter.
"""

import requests
import sys


if __name__ == "__main__":
    letter = ""

    if len(sys.argv) > 1:
        letter = sys.argv[1]

    record = {"q": letter}
    r = requests.post("http://0.0.0.0:5000/search_user", data=record)
    try:
        jsn = r.json()
        if jsn == {}:
            print("No result")
        else:
            print("[{}] {}".format(jsn.get("id"), jsn.get("name")))
    except ValueError:
        print("Not a valid JSON")
