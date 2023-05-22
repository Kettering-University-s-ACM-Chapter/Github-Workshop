# Author: Ku's ACM Chapter 2023

# This is a simple Python script that provides a function to perform addition.

# The 'sum' function takes two arguments, 'a' and 'b', and returns their sum.
# It's a simple demonstration of a function in Python and can be used as a starting point for more complex operations.

import sys

def math(a, b):
    """
    This function takes two numbers as input and returns their sum.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of 'a' and 'b'.
    """
    return a + b

# Testing the function:
if __name__ == "__main__":
    # sys.argv[0] is the script name itself, so we start from index 1
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print("The sum of {} and {} is: ".format(a, b), math(a, b))
    

