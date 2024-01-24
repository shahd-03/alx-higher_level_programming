#!/usr/bin/python3
def best_score(a_dictionary):
    t = list(a_dictionary.keys())[0]
    bigest_num = a_dictionary[t]
    for i, j in a_dictionary.items():
        if j > bigest_num:
            bigest_num = j
            t = i
    return (t)
