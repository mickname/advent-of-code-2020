#!/usr/bin/env python3
import collections
import re
import sys


def possible_containers(container_dict, bag_type):
    for outer in container_dict[bag_type]:
        yield outer
        yield from possible_containers(container_dict, outer)


def main():
    try:
        fname = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} input.txt", file=sys.stderr)
        return

    bag_containers = collections.defaultdict(set)

    with open(fname) as f:
        for line in f:
            outer, inner_str = line.split(' bags contain ', maxsplit=1)
            inner_bags = [
                match[1]
                for match in re.findall(r'(?P<count>\d+) (?P<bag_type>\w+ \w+) bags?', inner_str)
            ]
            for bag in inner_bags:
                bag_containers[bag].add(outer)

    unique_outer_containers = set(possible_containers(bag_containers, 'shiny gold'))
    print(f"Possible outer containers: {len(unique_outer_containers)}")


if __name__ == '__main__':
    main()
