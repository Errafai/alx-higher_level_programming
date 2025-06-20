#!/usr/bin/python3
"""fetches this  https://alx-intranet.hbtn.io/status using
requests package"""


if __name__ == "__main__":
    import requests as req

    url = "https://alx-intranet.hbtn.io/status"
    res = req.get(url)

    print('Body response:')
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
