#!/usr/bin/python3
""" Module Documentation"""



if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        cn = content.decode('utf-8')
        print("\t- utf8 ontent: {}".format(cn))
