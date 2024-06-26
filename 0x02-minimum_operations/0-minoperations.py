#!/usr/bin/python3
"""
Contains a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed to result in exactly
    n H characters in the file.
    """
    min_operations = 0
    operations = 2
    while n > 1:
        while n % operations == 0:
            min_operations += operations
            n /= operations
        operations += 1
    return min_operations
