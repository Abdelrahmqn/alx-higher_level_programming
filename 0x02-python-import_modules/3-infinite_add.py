#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) > 1:
        res = 0
        for args in argv[1:]:
            res += int(args)
        print(res)
