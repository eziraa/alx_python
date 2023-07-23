#!/bin/bash/python3
def no_c(string):
    list = ""

    for i in string:
        if i == 'c' or i == 'C':
            continue
        else:
            list += i

    return list
