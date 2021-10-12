#!/usr/bin/env python3

import random

CS = "BCDFGJKLMNPQSTVXZHRWY"
VS = "AEIOU"


def generate_name():
    result = ""
    for i in range(3):
        result += random.choice(CS)
        result += random.choice(VS)
    return result


if __name__ == "__main__":
    print(generate_name())
