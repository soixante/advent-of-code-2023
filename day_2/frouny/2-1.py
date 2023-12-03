#!/bin/env python3

import re

def remove_spaces(string):
    print(string.replace(" ", ""))
if __name__ == "__main__":
    starting_cubes = {"red":12, "green":13, "blue":14}
    red = 12
    green = 13
    blue = 14
    result = 0
    with open("input", "r") as data:
        for line in data.readlines():
            to_add = True
            val = re.match("^Game (\d+):(.*)$", line)
            game_number = int(val.group(1))
            games = val.group(2).split(";")
            for game in games:
                sets = game.split(',')
                for entry in sets:
                    matches = re.match("^(\d+) (\w+)$", entry.lstrip())
                    (cubes, color) = (int(matches.group(1)), matches.group(2))
                    if cubes > starting_cubes[color]:
                        to_add = False
            if to_add:
                result += int(game_number)
    print(result)
