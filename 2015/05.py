#!/usr/bin/env python3

import aoc
import re

_,lines = aoc.get_input(5)


nice_1 = re.compile(r"([aeiou].*){3,}")
nice_2 = re.compile(r"(\w)\1")
nice_3 = re.compile(r"ab|cd|pq|xy")

is_nice = lambda s: nice_1.search(s) is not None and nice_2.search(s) is not None and nice_3.search(s) is None

n_nice = sum([ is_nice(s) for s in lines ])

# Part 1: How many nice strings?
print(f"Part 1: {n_nice} nice strings")


neat_1 = re.compile(r"(..).*\1")
neat_2 = re.compile(r"(.).\1")

is_neat = lambda s: neat_1.search(s) is not None and neat_2.search(s) is not None

n_neat = sum([ is_neat(s) for s in lines ])

for l in lines:
  if is_neat(l):
    print(l)

# Part 2: How many nice strings according to the new criteria?
print(f"Part 1: {n_neat} nice strings")
