#!/usr/bin/python3
"""fetch a url and get the value of X-Request_Id
in the response header"""


if __name__ == "__main__":
    import requests as req
    import sys

    url = sys.argv[1]
    res = req.get(url)

    print(res.headers.get("X-Request-Id"))
