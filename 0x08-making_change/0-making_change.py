#!/usr/bin/python3
"""
Defines a solution to task: fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """ fewest number of coins needed to meet total """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        tmp = total // coin
        change += tmp
        total -= (tmp * coin)
    if total != 0:
        return -1
    return change
