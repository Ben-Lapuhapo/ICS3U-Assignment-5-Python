#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: Nov 2019
# This program uses finds the HCF of two numbers


def hcf():
    while True:
        # input
        num1 = input("Enter The First Number: ")
        num2 = input("Enter The Second Number: ")

        # process
        try:
            num1_integer = int(num1)
            num2_integer = int(num2)

            if num1_integer > num2_integer:
                smaller = num2_integer
            else:
                smaller = num1_integer
            for hcf in range(1, smaller + 1):
                if((num1_integer % hcf == 0) and (num2_integer % hcf == 0)):
                    answer = hcf
            print()
            print("The H.C.F. of {0} and {1} is: {2}"
                  .format(num1_integer, num2_integer, answer))

        except ValueError:
            print("Not A Number, Try Again")
            print()

        finally:
            print("Thank You For Playing!!")
            break


if __name__ == "__main__":
    hcf()
