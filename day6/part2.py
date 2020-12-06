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

    yes_answer_count = 0
    for g in groups:
        persons = iter(g.split('\n'))
        yes_questions = set(next(persons))
        for person in persons:
            if not person:
                # There's an extra line break at the end.
                break
            yes_questions.intersection_update(person)
        yes_answer_count += len(yes_questions)

    print(f"Count the number of questions to which everyone answered yes: {yes_answer_count}")


if __name__ == '__main__':
    main()
