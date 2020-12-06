#!/usr/bin/env python3
import sys


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

    trees = 0
    x = 0
    y = 0
    while y < height:
        x_wrap = x % width
        i = y * width + x_wrap
        if map[i]:
            trees += 1

        x += 3
        y += 1

    print(f"Trees encountered: {trees}")


if __name__ == '__main__':
    main()
