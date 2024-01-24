#!/usr/bin/python3
def uniq_add(my_list=[]):
    added = set(my_list)
    count = 0
    for i in added:
        count += i
    return count
