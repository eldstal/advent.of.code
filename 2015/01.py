#!/usr/bin/env python3

import aoc

raw,_ = aoc.get_input(1)


# Part 1: What floor does santa end up at?
a_floor = raw.count("(") - raw.count(")")
print(f"Part 1: floor {a_floor}")


# Part 2: How many instructions until santa ends up in the basement (-1)?
b_floor = 0
b_step=1
for move in raw:
  if move == "(": b_floor += 1
  if move == ")": b_floor -= 1
  if b_floor < 0: break
  b_step += 1

print(f"Part 2: step {b_step}")
