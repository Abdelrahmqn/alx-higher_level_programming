#!/usr/bin/python3
"""JSON"""


if __name__ == "__main__":
    import requests as r
    import json as j
    from sys import argv as a
    if len(a) == 1:
        q = ""
    else:
        q = a[1]

    dict_ = {'q': q}
    req = r.post('http://0.0.0.0:5000/search_user', data=dict_)
    dct_req = req.j()
    try:
        if dct_req == {}:
            print("No result")
        else:
            print("[{}] {}".format(dct_req.get("id"), dct_req.get("name")))
    except ValueError:
        print("Not a valid JSON")
