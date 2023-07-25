#!/usr/bin/python3
def raise_exception_msg(message=""):
    class CustomNameException(NameError):
        pass
    raise CustomNameException(message)
