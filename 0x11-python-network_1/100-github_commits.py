#!/usr/bin/python3
"""listing the last 10 commit of a repo and its owner"""


if __name__ == "__main__":
    import requests as req
    import sys

    url = "https://api.github.com/repos/"
    url +=  sys.argv[1] + "/" + sys.argv[2] + "/commits"
   
    for i in range(10):
        res = req.get(url)
        data = res.json()[0]
        sha = data["sha"]
        name = data["commit"]["author"]["name"]
        print("{}: {}".format(sha, name))
