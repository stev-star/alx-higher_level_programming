#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num = len(sys.argv) - 1  # Subtract 1 to exclude the script name
    if num == 0:  # check no of args and print accordingly
        print("{} arguments.".format('0'))
    elif num == 1:
        print("{} argument:".format(num))
    else:
        print("{} arguments:".format(num))

    for i in range(num):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
