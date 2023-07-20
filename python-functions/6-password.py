#!/bin/bash/python3
def validate_password(password):
    # Check length
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, and digits
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if not (has_uppercase and has_lowercase and has_digit):
        return False

    # Check for spaces
    if ' ' in password:
        return False

    # If all checks passed, return True
    return True
