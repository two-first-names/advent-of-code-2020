#!/usr/bin/env python3
import re

def is_password_valid(line):
    r = re.match(r'(\d+)\-(\d+) (.)\: (.+)', line)
    first_pos = int(r[1])
    second_pos = int(r[2])
    letter = r[3]
    password = r[4]

    return (password[first_pos - 1] == letter) ^ (password[second_pos - 1] == letter)

def main():
    with open('input') as f:
        print([is_password_valid(p) for p in f].count(True))


if __name__ == '__main__':
    main()
