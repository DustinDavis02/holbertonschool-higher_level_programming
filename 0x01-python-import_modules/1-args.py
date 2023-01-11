#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    n = len(argv)

if n == 0:
    print("{} arguments.\n".format(n))
elif n == 1:
    print("{} argument:\n".format(n))
else:
    print("{} arguments:\n".format(n))

for i in range(n):
    print("{}. {}\n".format(i + 1, argv[i]))
