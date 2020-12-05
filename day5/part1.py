#!/usr/bin/env python3
import sys


def main():
    try:
        fname = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} input.txt", file=sys.stderr)
        return

    max_seat_id = 0
    with open(sys.argv[1]) as f:
        for line in f:
            row = int(line[0:7].replace('F', '0').replace('B', '1'), 2)
            col = int(line[7:10].replace('L', '0').replace('R', '1'), 2)
            seat_id = 8 * row + col

            max_seat_id = max(max_seat_id, seat_id)

    print(f"Max seat id: {max_seat_id}")


if __name__ == '__main__':
    main()
