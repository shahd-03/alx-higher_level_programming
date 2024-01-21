#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    updated_tuple = ()
    tuple_new1 = tuple_a + (0, 0)
    tuple_new2 = tuple_b + (0, 0)
    updated_tuple = tuple_new1[0] + tuple_new2[0], tuple_new1[1] + tuple_new2[1]
    return updated_tuple
