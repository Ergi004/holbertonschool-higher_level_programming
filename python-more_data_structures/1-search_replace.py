#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for char in range(len(new_list)):
        if new_list[char] == search:
            new_list[char] = replace
    return new_list
