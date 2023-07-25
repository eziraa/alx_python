#!/usr/bin/python3
def raise_exception_msg(message=""):
    class CustomNameException(Exception):
        pass
    # if not message:
    raise CustomNameException(message)
