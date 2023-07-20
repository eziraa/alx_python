#!/bin/bash/python3
def pow(a, b):
    if b == 0:
        return 1
    if (b > 0):
        for i in range(b):
            a = a * a
    else:
        for i in range(-b):
            a = a / a
    return a
