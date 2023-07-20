#!/bin/bash/python3
def fibonacci_sequence(n):
    list = []
    if n > 0:
        if (n == 1):
            list.append(0)
        elif (n == 2):
            list.append(0)
            list.append(1)
        else:
            i = 2
            list.append(0)
            list.append(1)
            while (i < n):
                list.append(list[i-1] + list[i - 2])
                i = i + 1

    return list
