#!/usr/bin/env python3
from itertools import combinations

def main():
    with open('input') as f:
        input_numbers = [int(n) for n in f]
        combs = combinations(input_numbers, 2)
        result = [x * y for x, y in combs if x + y == 2020][0]
        print(result)

if __name__ == '__main__':
    main()
