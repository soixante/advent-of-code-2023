#!/bin/env python3

def get_left(string):
    """ function returning first digit from left """
    iterator = 0
    while iterator != len(string):
        if string[iterator].isdecimal():
            return string[iterator]
        iterator += 1
def get_right(string):
    """ function returning first digit from left """
    iterator = len(string) - 1
    while iterator >= 0:
        if string[iterator].isdecimal():
            return string[iterator]
        iterator -= 1


if __name__ == "__main__":
    final_res = 0
    with open("input", "r") as input_file:
        for line in input_file.readlines():
            number = get_left(line)
            number += get_right(line)
            final_res += int(number)
    print(final_res)
