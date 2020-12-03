#!/usr/bin/env python3

def main():
    lines = []
    with open('input') as f:
        for l in f:
            lines.append(list(l.strip()))

    end = len(lines)
    line_len = len(lines[0])

    x = 0
    y = 0

    trees = 0

    while y < end:
        char = lines[y][x]
        if char == '#':
            trees += 1
            lines[y][x] = 'X'
        else:
            lines[y][x] = 'O'
        x = (x + 3) % line_len
        y = y + 1

    print(trees)

if __name__ == '__main__':
    main()