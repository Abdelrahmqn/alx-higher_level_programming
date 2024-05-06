#!/usr/bin/python3
"""Error"""

if __name__ == "__main__":
    import requests as r
    from sys import argv as a
    from requests.exceptions import HTTPError

    try:
        req = r.get(a[1])
    except HTTPError as f:
        print("Error code: {}".format(f.response.status_code))
