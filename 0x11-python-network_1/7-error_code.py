#!/usr/bin/python3
"""Error"""

if __name__ == "__main__":
    import requests as r
    from sys import argv as a

    req = r.get(a[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
