#!/usr/bin/python3
"""send a post request with an email data"""


if __name__ == "__main__":
    import requests as req
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    res = req.post(url, data={"email": email})
