#!/usr/bin/env python3
import sys


def check_slope(map, width, height, dx, dy):
    trees = 0
    x = 0
    y = 0
    while y < height:
        x_wrap = x % width
        i = y * width + x_wrap
        if map[i]:
            trees += 1

        x += dx
        y += dy
    return trees


def main():
    try:
        fname = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} input.txt", file=sys.stderr)
        return

    with open(fname) as f:
        width = len(f.readline().rstrip('\n'))
        f.seek(0)
        height = 0
        map = []
        for line in f:
            line = line.rstrip('\n')
            map.extend([tile == '#' for tile in line])
            height += 1

    slopes_to_check = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    answer = 1
    for dx, dy in slopes_to_check:
        trees = check_slope(map, width, height, dx, dy)
        print(f"Trees encountered for slope {dx}, {dy}: {trees}")
        answer *= trees

    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()
