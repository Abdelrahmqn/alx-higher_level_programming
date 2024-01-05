#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_num = len(sys.argv) - 1
    if arg_num < 1:
        print("{} arguments.".format(arg_num))
    elif arg_num == 1:
        print("{} argument:".format(arg_num))
    else:
        print("{} arguments:".format(arg_num))
        for j in range(arg_num):
            print("{}: {}".format(j + 1, sys.argv[j + 1]))
