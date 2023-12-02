#!/bin/env python3
import re, sys
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'calibration'

f=open(filename, "r")
somme=0
numbers = {"one": "1", "two" : "2", "three":"3", "four": "4", "five": "5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
for num in f:
    print(num)
    for i in range(0, len(num)):
        for number in numbers.keys():
            if num[i:].startswith(number):
                num=num[0:i]+numbers[number]+num[i+1:]
    print(num)
    num=re.sub("[^0-9]", "", num)
    print(num)
    somme+=int(num[0]+num[-1])

print("SOMME : " + str(somme))
