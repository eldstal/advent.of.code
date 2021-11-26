#!/usr/bin/env python3

import aoc
import re
import numpy as np

_,lines = aoc.get_input(6)

PARSER = re.compile(r"(?P<op>turn on|turn off|toggle) (?P<x0>[0-9]+),(?P<y0>[0-9]+) through (?P<x1>[0-9]+),(?P<y1>[0-9]+)")

def parse(operation):
  m = PARSER.match(operation)
  if m is None:
    raise operation

  return ( m.group("op"),
           int(m.group("x0")),
           int(m.group("y0")),
           int(m.group("x1")),
           int(m.group("y1"))
         )

def round_1(grid, operation):
  op,x0,y0,x1,y1 = parse(operation)

  old = grid[y0:y1+1, x0:x1+1]
  if op == "turn on":
    new = 1
  elif op == "turn off":
    new = 0
  elif op == "toggle":
    new = np.logical_not(old)
  else:
    raise RuntimeError(op)

  grid[y0:y1+1, x0:x1+1] = new

def round_2(grid, operation):
  op,x0,y0,x1,y1 = parse(operation)

  old = grid[y0:y1+1, x0:x1+1]
  if op == "turn on":
    new = old + 1
  elif op == "turn off":
    new = old - 1
    new = np.clip(new, 0, None)
  elif op == "toggle":
    new = old + 2
  else:
    raise RuntimeError(op)

  grid[y0:y1+1, x0:x1+1] = new


grid = np.ndarray((1000,1000), dtype=bool)
grid[:,:] = 0

for l in lines:
  round_1(grid, l)

print(f"Part 1: {np.sum(grid)} lights")


grid = np.ndarray((1000,1000), dtype=int)
grid[:,:] = 0

for l in lines:
  round_2(grid, l)

print(f"Part 2: {np.sum(grid)} total brightness")
