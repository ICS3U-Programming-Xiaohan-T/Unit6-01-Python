#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: May 16, 2025
# This program finds the average of 10 random numbers in a range and prints it

import random
import const


def main():
    # Initialize variables to zero
    sum = 0
    # Create a list to store the grades
    grade = []

    # Use a for loop to generate 10 random numbers
    for num in range(10):
        # Generate a random number between the constants defined in const.py
        random_num = random.randint(const.MIN, const.MAX)
        # Append the random number to the list
        grade.append(random_num)
        # Print the random number
        print("The grade is:", random_num)

    # Calculate the average of the numbers in the list use a for loop
    for counter in range(10):
        # Add each number in the list to the sum
        sum = sum + grade[counter]

    # Calculate the average
    average = sum / 10
    # Print the average
    print("The average is:", average)


if __name__ == "__main__":
    main()
