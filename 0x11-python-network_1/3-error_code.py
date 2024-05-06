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
            print(response.read().decode('utf-8'))
    except HTTPError as f:
        print("Error code: {}".format(f.code))
        print("Error code: {}".format(f.reason))
        print("Error code: {}".format(f.headers))
