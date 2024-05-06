#!/usr/bin/python3
"""a POST request to the passed
URL with the email as a parameter,
and finally displays the body of the response."""


if __name__ == "__main__":
    from sys import argv as a
    import requests as r
    url = a[1]
    email = a[2]
    d = ({'email': email})
    re = r.post(url, data=d)

    print(re.text)
