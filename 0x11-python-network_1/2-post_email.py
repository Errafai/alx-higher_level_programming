#!/usr/bin/python3
"""send a post request using an url and email as arguments
with email as data"""


if __name__ == "__main__":
    import urllib.request as req
    import urllib.parse as parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    data = parse.urlencode(data).encode("ascii")
    request = req.Request(url, data)

    with req.urlopen(request) as res:
        print(res.read().decode("utf-8"))
