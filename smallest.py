#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: oct 2021
# this function generates 10 random numbers and finds the smallest one
import random


def smallest_finder(number_list):
    # This function finds the smallest number of an array

    smallest = number_list[9]

    for loop_item in number_list:
        if loop_item < smallest:
            smallest = loop_item
        else:
            smallest = smallest
    return smallest


def main():
    # This function generates 10 random numbers

    number_list = []

    for loop_counter in range(0, 10):
        random_number = random.randint(0, 100)
        number_list.append(random_number)
        print("The random number is: {}".format(random_number))

    smallest_number = smallest_finder(number_list)

    print("\n\nThe smallest number is {}".format(smallest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
