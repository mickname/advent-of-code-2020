#!/usr/bin/env python3
import re
import sys


def main():
    try:
        fname = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} input.txt", file=sys.stderr)
        return

    with open(fname) as f:
        # Lines are like "2-9 c: ccccccccc"
        iter_parsed = (
            re.fullmatch(r'(?P<minoccur>\d+)-(?P<maxoccur>\d+) (?P<letter>.): (?P<password>.+)\n',
                         line)
            for line in f
        )

        num_valid = 0
        for parsed in iter_parsed:
            minoccur, maxoccur, letter, password = parsed.groups()
            occurences = list(password).count(letter)
            if occurences >= int(minoccur) and occurences <= int(maxoccur):
                num_valid += 1

    print(f"Number of valid passwords: {num_valid}")


if __name__ == '__main__':
    main()
