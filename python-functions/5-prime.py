#!/bin/bash/python3
def is_prime(number):
    i = 2
    count = 0
    while (i < number):
        if (number % i == 0):
            count += 1
        i = i + 1

    if (count == 0):
        return "True"

    return "False"
