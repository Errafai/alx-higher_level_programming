#!/usr/bin/python3
"""this script takes an URL as argument and show the X-request-Id
variable found in the header of the response"""

if __name__ == "__main__":
    import urllib.request as req
    import sys

    url = sys.argv[1]

    with req.urlopen(url) as res:
        print(res.getheader("X-Request-Id"))
