#!/usr/bin/env python3
import math

def main():
    lines = []
    with open('input') as f:
        for l in f:
            lines.append(list(l.strip()))

    end = len(lines)
    line_len = len(lines[0])

    def get_trees_for_slope(right, down):
        x = 0
        y = 0

        trees = 0

        while y < end:
            char = lines[y][x]
            if char == '#':
                trees += 1
            x = (x + right) % line_len
            y = y + down

        return trees

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    slope_trees = [get_trees_for_slope(right, down) for right, down in slopes]

    print(slope_trees)
    
    print(math.prod(slope_trees))


if __name__ == '__main__':
    main()