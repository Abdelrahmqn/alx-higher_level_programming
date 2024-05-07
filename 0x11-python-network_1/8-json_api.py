#!/usr/bin/python3
"""JSON"""


if __name__ == "__main__":
    import requests as r
    import json as j
    from sys import argv as a
    if len(a[1]):
        q = a[1]
    else:
        q = ""

    dict_ = {'q': q}
    req = r.post('http://0.0.0.0:5000/search_user', data=dict_)
    dct_req = req.j()
    try:
        if dct_req:
            print("[{}] {}".format(dct_req['id'], dct_req['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
