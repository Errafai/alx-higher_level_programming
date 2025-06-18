#!/usr/bin/python3
"""feches https://alx-intranet.hbtn.io/status and display response"""


if __name__ == "__main__":
    import urllib.request as rq

    url = "https://alx-intranet.hbtn.io/status"
    with rq.urlopen(url) as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
