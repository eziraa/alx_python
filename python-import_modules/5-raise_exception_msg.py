#!/usr/bin/python3
def raise_exception_msg(message=""):
    class CustomNameException(NameError):
        pass
    # if not message:
    try:
        raise CustomNameException(message)
    except CustomNameException:
        pass


try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
