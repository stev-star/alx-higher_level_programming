#!/usr/bin/python3

if __name__ == "__main__":
# import the module required
    from add_0 import add

    a = 1
    b = 2
# generate the required results
result = add(a,b)

# print the results
print("{:d} + {:d} = {:d}".format(a, b, result))
