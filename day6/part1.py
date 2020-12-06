#!/usr/bin/env python3
import sys


def main():
    try:
        fname = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} input.txt", file=sys.stderr)
        return

    with open(fname) as f:
        groups = f.read().split('\n\n')

    yes_answers_for_group = (len(set(g.replace('\n', ''))) for g in groups)
    answer = sum(yes_answers_for_group)
    print(f"Sum of counts: {answer}")


if __name__ == '__main__':
    main()
