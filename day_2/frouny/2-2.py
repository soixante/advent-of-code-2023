#!/bin/env python3

import re

def remove_spaces(string):
    print(string.replace(" ", ""))
if __name__ == "__main__":
    result = 0
    with open("input", "r") as data:
        for line in data.readlines():
            max_green = 1
            max_red = 1
            max_blue = 1
            val = re.match("^Game (\d+):(.*)$", line)
            game_number = int(val.group(1))
            games = val.group(2).split(";")
            for game in games:
                sets = game.split(',')
                for entry in sets:
                    matches = re.match("^(\d+) (\w+)$", entry.lstrip())
                    (cubes, color) = (int(matches.group(1)), matches.group(2))
                    if color == "green":
                        if max_green < cubes:
                            max_green = cubes
                    if color == "red":
                        if max_red < cubes:
                            max_red = cubes
                    if color == "blue":
                        if max_blue < cubes:
                            max_blue = cubes
            result += max_green*max_blue*max_red
            print(max_red, max_green, max_blue, max_green*max_blue*max_red, result)
    print(result)
