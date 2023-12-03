#!/bin/env python3
import re

def get_left_number(string):
    """ function returning first digit from left """
    iterator = 0
    while iterator != len(string):
        if string[iterator].isdecimal():
            return iterator
        iterator += 1
    return -1
def get_right_number(string):
    """ function returning first digit from left """
    iterator = 0
    while iterator != len(string):
        if string[iterator].isdecimal():
            return iterator
        iterator += 1
    return -1
def get_left_alpha_number(string):
    numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5",
    "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    res = dict()
    for alphanum in numbers:
        index = string.find(alphanum)
        if index >= 0:
            res[index] = numbers[alphanum]
    if len(res) > 0:
        temp = sorted(res.keys())
        first = temp.pop(0)
        return (first, res[first])
    else:
        return (-1,None)
    return (index, res[index])
def get_right_alpha_rev_numbers(string):
    numbers = {"eno":"1", "owt":"2", "eerht":"3", "ruof":"4", "evif":"5",
    "xis":"6", "neves":"7", "thgie":"8", "enin":"9"}
    res = dict()
    for alphanum in numbers:
        index = string.find(alphanum)
        if index >= 0:
            res[index] = numbers[alphanum]
    if len(res) > 0:
        temp = sorted(res.keys())
        first = temp.pop(0)
        return(len(string) - 1 - first, res[first])
    else:
        return (-1,None)
    return (index, res[index])


if __name__ == "__main__":
    final_res = 0
    with open("input", "r") as input_file:
        for line in input_file.readlines():
            (left_alpha_index, left_alpha_value) = get_left_alpha_number(line)
            left_number_index = get_left_number(line)
            if left_alpha_index == -1:
                number = line[left_number_index]
            elif left_alpha_index < left_number_index:
                number = left_alpha_value
            else:
                number = line[left_number_index]
            right_number_index = get_right_number(line[::-1])
            right_number_index = len(line) - 1 - right_number_index
            (right_alpha_index, right_alpha_value) = get_right_alpha_rev_numbers(line[::-1])
            if right_alpha_index == -1 and right_number_index == -1:
                number += number
            if right_alpha_index == -1:
                number += line[right_number_index]
            elif right_number_index == -1:
                number += right_alpha_value
            else:
                if right_alpha_index > right_number_index:
                    number += right_alpha_value
                else:
                    number += line[right_number_index]
            print(line, number)
            final_res += int(number)
    print(final_res)
