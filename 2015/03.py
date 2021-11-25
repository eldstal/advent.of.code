#!/usr/bin/env python3

import aoc

raw,_ = aoc.get_input(3)


move = {
          "<": lambda x,y: (x-1, y),
          "^": lambda x,y: (x  , y+1),
          ">": lambda x,y: (x+1, y),
          "v": lambda x,y: (x  , y-1),
       }

def run(commands, houses):

  x=0
  y=0

  # Always deliver to the starting house as well
  if (x,y) not in houses: houses[(x,y)] = 0
  houses[(x,y)] += 1

  for step in commands:
    x,y = move[step](x,y)
    if (x,y) not in houses: houses[(x,y)] = 0
    houses[(x,y)] += 1

  return houses


houses = run(raw, {})
a_visited = sum([ c>0 for c in houses.values() ])

# Part 1: How many houses received at least one present?
print(f"Part 1: {a_visited} houses")



santa_houses = run(raw[0::2], {})
robot_houses = run(raw[1::2], santa_houses)

b_visited = sum([ c>0 for c in robot_houses.values() ])

# Part 1: How many houses received at least one present?
print(f"Part 2: {b_visited} houses")
