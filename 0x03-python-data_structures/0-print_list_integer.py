#!/usr/bin/python3
def print_list_integer(my_list = []):
    # loop through each value in my_list
    for x in my_list:
        print("{}".format(x))

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
