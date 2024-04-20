#!/usr/bin/python3
""" A script that defines a function to determine
if a list of boxes can open each other.
"""


def canUnlockAll(boxes):
    """ Returns True if all boxes can be unlocked.
    """
    keys = list(boxes[0])
    unlocked = [0]

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            unlocked.append(key)
            keys.extend(boxes[key])

    return len(unlocked) == len(boxes)
