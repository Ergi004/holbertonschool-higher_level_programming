#!/usr/bin/python3
def uniq_add(my_list=[]):
    for i in my_list:
        if i in my_list != 1:
            return sum(my_list[2:])
