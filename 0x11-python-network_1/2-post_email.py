#!/usr/bin/python3
"""sends Post request to url with email as a parameter
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    import sys
    from urllib.parse import urlencode

    email = sys.argv[2]
    email_data = urlencode({'email': email}).encode('utf-8')
    with urlopen(sys.argv[1], data=email_data) as res:
        print(res.read().decode('utf-8'))
