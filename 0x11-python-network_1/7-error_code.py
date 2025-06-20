#!/usr/bin/python3
"""send a requet to the url and esplay the body
of the response"""


if __name__ == "__main__":
    import requests as req
    import sys

    url = sys.argv[1]
    
    res = req.get(url)
    print(res.text)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
