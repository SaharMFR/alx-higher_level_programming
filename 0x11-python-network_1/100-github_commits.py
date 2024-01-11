#!/usr/bin/python3
"""
Takes 2 arguments in order to solve this challenge:
    * Listing 10 commits (from the most recent to oldest) of the repository
      "rails" by the user "rails", using the GitHub API.
    * Printing all commits by: `<sha>: <author name>` (one by line).
The first argument is `repository name`, and the second is `owner name`.
"""

import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]))
    cmts = r.json()
    try:
        for i in range(0, 10):
            print("{}: {}".format(cmts[i].get("sha"),
                  cmts[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
