"""
File: hailstone.py
Author:
Date:
Section:
E-mail:
Description: This file contains python code that implements the "flight"
  of a hailstone, following the HOTPO rules (also known as the Collatz
  Conjecture), recursively
"""

# NO CONSTANTS NEEDED, THE NUMBERS USED IN flight() ARE
#    PART OF A FORMULA/MATHEMATICAL CONJECTURE

def flight(hieght):
    """
    recursively calculates the path of a hailstone
    :param height: the height of the hailstone
    :return: a recursive call, which at the end returns the number
        of "steps"taken for the hailstone to reach a height of 1
    """

    #### BASE CASES:
    # if height is zero or lower, print out an "invalid" message and return 0
    if hieght <= 0 :
        print("invalid hieght of ", hieght)
        return 0
    else:
        print("hieght of", hieght)
        if hieght>1:

        # recursive case
            if hieght%2 ==0:
                return 1 + flight(hieght/2)
            
            elif hieght %2 != 0:
                return 1 + flight(hieght*3+1)
        else:
            return 0
    # stops when it reachs height of 1 (the ground)

    #### RECURSIVE CASES:
    # if the current height is even, divide it by 2

    # if the current height is odd, multiply it by 3, then add 1


if __name__ == "__main__":

    print("Welcome to the Hailstone Simulator!")
    msg = "Please enter a height for the hailstone to start at: "
    start_height = int(input(msg))

    # recursive call goes here
    steps  = flight(start_height)

    print("\nIt took", steps, "steps to hit the ground.")
    print("Thank you for using the Hailstone Simulator!\n")

