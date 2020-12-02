#!/usr/bin/env python3
import re
import sys


def main():
    try:
        fname = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} input.txt", file=sys.stderr)
        return

    with open(sys.argv[1]) as f:
        # Lines are like "2-9 c: ccccccccc"
        iter_parsed = (
            re.fullmatch(r'(?P<pos1>\d+)-(?P<pos2>\d+) (?P<letter>.): (?P<password>.+)\n',
                         line)
            for line in f
        )

        num_valid = 0
        for parsed in iter_parsed:
            pos1, pos2, letter, password = parsed.groups()
            i1, i2 = int(pos1) - 1, int(pos2) - 1
            if ((password[i1] == letter) != (password[i2] == letter)):
                num_valid += 1

    print(f"Number of valid passwords: {num_valid}")


if __name__ == '__main__':
    main()
