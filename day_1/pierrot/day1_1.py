#!/bin/env python3
import re
f=open("calibration", "r")
sum=0
for line in f:
    num=re.sub("[^0-9]", "", line)

    print(line.strip(), num, num[0]+num[-1])
    numline = num[0]+num[-1]
    sum+=int(numline)

print("SOMME : " + str(sum))
