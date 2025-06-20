#!/usr/bin/python3
"""a Post request that send a letter with the letter as a parameter"""


if __name__ == "__main__":
    import requests as req
    import sys

    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) == 1 is not None else ""
    res = req.post(url, data={"q": q})

    try:
        res = res.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))

    except ValueError:
        print("Not a valid JSON")
