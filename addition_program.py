#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Oct 2022
# This program adds two numbers together


def main():
    # This function adds up two numbers

    # input
    first_number = int(input("Enter the first number:"))
    second_number = int(input("Enter the second number:"))

    # process
    answer = first_number + second_number

    # output
    print("")
    print("{0} + {1} = {2}.".format(first_number, second_number, answer))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
