#!/usr/bin/env python3
import re
import sys

REQUIRED_FIELDS = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid',
}


def main():
    try:
        fname = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} input.txt", file=sys.stderr)
        return

    with open(sys.argv[1]) as f:
        passports = f.read().split('\n\n')

    num_valid = 0

    for p in passports:
        fields_values = [f for f in re.split(r'[ \n]', p) if f]

        field_names = {
            f.split(':')[0] for f in fields_values
        }

        if len(field_names.intersection(REQUIRED_FIELDS)) == len(REQUIRED_FIELDS):
            num_valid += 1

    print(f"Number of valid passports: {num_valid}")


if __name__ == '__main__':
    main()
