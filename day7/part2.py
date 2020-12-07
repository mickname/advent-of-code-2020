#!/usr/bin/env python3
import collections
import re
import sys


def number_contained(contain_dict, bag_type):
    '''Count contained bags recursively.
    '''
    return sum(
        count + count * number_contained(contain_dict, inner_bag)
        for count, inner_bag in contain_dict[bag_type]
    )


def main():
    try:
        fname = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} input.txt", file=sys.stderr)
        return

    bag_contains = collections.defaultdict(list)

    with open(fname) as f:
        for line in f:
            outer, inner_str = line.split(' bags contain ', maxsplit=1)
            inner_bags = [
                (int(match[0]), match[1])
                for match in re.findall(r'(?P<count>\d+) (?P<bag_type>\w+ \w+) bags?', inner_str)
            ]
            bag_contains[outer].extend(inner_bags)

    answer = number_contained(bag_contains, 'shiny gold')
    print(f"A shiny gold bag contains {answer} other bags.")


if __name__ == '__main__':
    main()
