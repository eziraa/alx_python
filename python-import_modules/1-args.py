#!/bin/bash/python3
import sys


def print_arguments():
    # Exclude the first element (script name) from the list
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    # Print the number of arguments and the list of arguments
    print(num_arguments, "argument" if num_arguments ==
          1 else "arguments", end="")

    if num_arguments == 0:
        print(".", end="\n")
    else:
        print(":", end="\n")

        # Print one line per argument along with its position and value
        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    print_arguments()
