#!/usr/bin/python3
import sys


def factorize(num):
    """ Generate 2 factors for a given number"""
    i = 2
    while (num % i):
        if (i <= num):
            i += 1

    k = num // i
    return (k, i)


if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

filename = sys.argv[1]

file = open(filename, 'r')
lines = file.readlines()

for line in lines:
    num = int(line.rstrip())
    k, i = factorize(num)
    print(f"{num} = {k} * {i}")