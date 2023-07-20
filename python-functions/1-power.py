#!/bin/bash/python3
def pow(a, b):
    result = 1.0
    if b == 0:
        return 1
    elif (b > 0):
        i = 0
        while (i < b):
            result = result * a
            i += 1
    else:
        i = 0
        while (i > b):
            result = result / a
            i -= 1
    return result
