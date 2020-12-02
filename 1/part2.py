#!/usr/bin/env python3
from itertools import combinations

def main():
    with open('input') as f:
        input_numbers = [int(n) for n in f]
        combs = combinations(input_numbers, 3)
        result = [x * y * z for x, y, z in combs if x + y + z == 2020][0]
        print(result)

if __name__ == '__main__':
    main()
