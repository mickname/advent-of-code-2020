#!/usr/bin/env python3
import sys


def main():
    try:
        fname = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} input.txt", file=sys.stderr)
        return

    boarding_pass_found = (8 * 128) * [False]

    with open(sys.argv[1]) as f:
        for line in f:
            row = int(line[0:7].replace('F', '0').replace('B', '1'), 2)
            col = int(line[7:10].replace('L', '0').replace('R', '1'), 2)
            seat_id = 8 * row + col

            boarding_pass_found[seat_id] = True

    for i in range((8 * 128) - 2):
        if boarding_pass_found[i:i + 3] == [True, False, True]:
            break
    else:
        raise ValueError("Couldn't find seat :(")

    my_seat = i + 1
    print(f"My seat id: {my_seat}")


if __name__ == '__main__':
    main()
