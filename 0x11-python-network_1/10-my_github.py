#!/usr/bin/python3
"""
Takes your GitHub credentials (usrname and password) and uses `GitHub API`
to display your `id`. Uses Basic Authentication with a personal access token
as password to access to your information.
"""

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    authentication = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=authentication)
    print(r.json().get("id"))
