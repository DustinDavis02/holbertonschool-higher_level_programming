#!/usr/bin/python3
for i in range(10):
    for n in range(i+1,10):
        print("{:01d}{:01d}".format(i, n), end=", ")
    if i == 9:
        print("\n",end='')
