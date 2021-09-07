#!/usr/bin/python3


def islower(c):
    for i in range(97, 123):
        if chr(i) == c:
            return bool(1)
    return bool(0)
