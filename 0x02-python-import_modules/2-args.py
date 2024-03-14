#!/usr/bin/python3

import sys

n = len(sys.argv[1:])
if n == 1:
    print(f"{n} argument:")
else:
    print(f"{n} arguments:")
for i, arg in enumerate(sys.argv[1:]):
    print(f"{i}: {arg}")
