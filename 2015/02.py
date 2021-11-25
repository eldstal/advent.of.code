#!/usr/bin/env python3

import aoc
import itertools

_,lines = aoc.get_input(2)

dims = [ [ int(x) for x in l.split("x") ] for l in lines ]

a_area = 0
for box in dims:
  pieces = [ a*b for a,b in itertools.combinations(box, 2) ]
  slack = min(pieces)
  area = 2*sum(pieces) + slack
  a_area += area


# Part 1: How much paper?
print(f"Part 1: {a_area} sqft")


b_length = 0

for box in dims:
  sides = [ 2*a+2*b for a,b in itertools.combinations(box, 2) ]
  circ = min(sides)
  bow = box[0] * box[1] * box[2]
  length = circ + bow
  b_length += length

print(f"Part 2: {b_length} ft")
