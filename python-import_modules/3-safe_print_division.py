#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('The divisor should be non zero')
        return None
    except TypeError:
        print('The number should both integer')
        return None
    finally:
        print("Inside result: {}".format(a / b if b > 0 else None))
