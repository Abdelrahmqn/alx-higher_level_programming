#!/usr/bin/python3
"""
   send a req to url
   dispalys the of the response
   Manage urllib.error.HTTPError exceptions
"""


if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    import sys

    try:
        with urlopen(sys.argv[1]) as response:
            print(response.decode('utf-8'))
    except HTTPError as f:
        print(f.code)
        print(f.reason)
        print(f.headers)
        if f.fp is not None:
            print(f.fp.read().decode('utf-8'))
