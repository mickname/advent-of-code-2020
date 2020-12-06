#!/usr/bin/env python3
import functools
import itertools
import operator
import sys


def main():
    try:
        _, fname, num_numbers = sys.argv
        num_numbers = int(num_numbers)
    except (ValueError, IndexError):
        print(f"Usage: {sys.argv[0]} input.txt NUMBER_OF_ENTRIES_TO_SUM", file=sys.stderr)
        return

    with open(fname) as f:
        iter_numbers = (int(line) for line in f)
        for numbers in itertools.combinations(iter_numbers, num_numbers):
            if sum(numbers) == 2020:
                product = functools.reduce(operator.mul, numbers)
                print(f"Entries: {' + '.join((str(num) for num in numbers))} == 2020")
                print(f"Answer: {product}")
                return


if __name__ == '__main__':
    main()
