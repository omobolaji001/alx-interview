#!/usr/bin/python3

""" A script to determines if a given data
    set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding, else return False.

    Args:
        data (List[int]): list of integers representing bytes in the data set.
    """
    mask_1 = 1 << 7
    mask_2 = 1 << 6
    continuation_byte = 0

    for byte in data:
        mask = 1 << 7
        # In case we are not expecting a continuation byte
        if continuation_byte == 0:
            # check the number of 1's we have in the MSB
            # This determines how many continuation bytes
            # we are to expect
            while byte & mask:
                continuation_byte += 1
                mask = mask >> 1

            # If the byte is a 1-byte, then we contiue the loop
            if continuation_byte == 0:
                continue
            # If the continuation byte is 1 or 4, then it has violated
            # the UTF8 rule
            if continuation_byte == 1 or continuation_byte > 4:
                return False
        else:
            # In the case where continuation_byte is present
            # we check if it fulfills the rule of UTF8 that says
            # it must be continued with the MSB being `10`
            if not (byte & mask_1 and not (byte & mask_2)):
                return False

        # After making sure the rule is fulfilled
        # we decrement the continuation byte
        continuation_byte -= 1

    return continuation_byte == 0
