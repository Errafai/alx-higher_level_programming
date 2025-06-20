#!/usr/bin/python3
"""dispalys the body of the response passed as argv"""


if __name__ == "__main__":
    import urllib.error as err
    import urllib.request as req
    import sys

    try:
        url = sys.argv[1]
        with  req.urlopen(url) as res:
            print(res.read())
    except err.HTTPError as e:
        print("Error code: ", e.code)
