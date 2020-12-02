#!/usr/bin/env python3
import re

def is_password_valid(line):
    r = re.match(r'(\d+)\-(\d+) (.)\: (.+)', line)
    min_count = int(r[1])
    max_count = int(r[2])
    letter = r[3]
    password = r[4]

    count = password.count(letter)
    return count >= min_count and count <= max_count

def main():
    with open('input') as f:
        print([is_password_valid(p) for p in f].count(True))


if __name__ == '__main__':
    main()
