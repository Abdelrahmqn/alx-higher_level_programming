#!/usr/bin/python3
"""request from url"""


if __name__ == "__main__":
    import requests

    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    if req.status_code == 200:
        print("\t- content: {}".format(req.status_code))
