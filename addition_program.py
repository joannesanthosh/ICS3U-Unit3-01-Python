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
    print("The answer is {0}.".format(answer))


if __name__ == "__main__":
    main()
