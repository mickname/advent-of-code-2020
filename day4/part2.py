#!/usr/bin/env python3
import re
import sys


def height_validate(val):
    m = re.fullmatch(r'(\d+)(cm|in)', val)
    if not m:
        return False
    num = int(m.group(1))
    unit = m.group(2)
    if unit == 'cm':
        return num >= 150 and num <= 193
    elif unit == 'in':
        return num >= 59 and num <= 76
    return False


FIELD_VALIDATORS = [
    ('byr', lambda x: int(x) >= 1920 and int(x) <= 2002),
    ('iyr', lambda x: int(x) >= 2010 and int(x) <= 2020),
    ('eyr', lambda x: int(x) >= 2020 and int(x) <= 2030),
    ('hgt', height_validate),
    ('hcl', lambda x: bool(re.fullmatch(r'#[0-9a-f]{6}', x))),
    ('ecl', lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}),
    ('pid', lambda x: bool(re.fullmatch(r'[0-9]{9}', x))),
    # 'cid',
]


def main():
    try:
        fname = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} input.txt", file=sys.stderr)
        return

    with open(fname) as f:
        passports = f.read().split('\n\n')

    num_valid = 0

    for p in passports:
        fields = {
            n: v for n, v in (f.split(':', maxsplit=1) for f in re.split(r'[ \n]', p) if f)
        }

        for field_name, validator_fn in FIELD_VALIDATORS:
            try:
                if not validator_fn(fields[field_name]):
                    break
            except KeyError:
                break
        else:
            num_valid += 1

    print(f"Number of valid passports: {num_valid}")


if __name__ == '__main__':
    main()
