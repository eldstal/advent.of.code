import aoc

import statistics
import numpy as np

DAY=7

raw, _ = aoc.get_input(DAY)
#raw, _ = aoc.get_test_input(DAY)

answer_a = 0

positions = [ int(c.strip()) for c in raw.split(",") ]

def linear_goal(positions):
  positions = sorted(positions)
  n = len(positions)
  return positions[n//2]

def linear_cost(positions, goal):
  return sum([abs(p - goal) for p in positions])

print(positions)
goal = linear_goal(positions)

answer_a = linear_cost(positions, goal)

print(f"Part 1: {answer_a}")
#print(aoc.post_result(day=DAY, part=1, value=answer_a, year=2021))


def fuel(dist):
  return (dist*(dist+1))//2

def exp_goal(positions):
  l = min(positions)
  u = max(positions)

  w = u-l+1
  h = len(positions)
  mat = np.ndarray((h, w))

  for y in range(h):
    pt = positions[y]  # The point represented by this row
    for x in range(w):
      pos = l + x   # The actual X coordinate of this cell
      mat[y,x] = fuel(abs(pos-pt))

  # Now sum up the rows to get the fuel cost of each possible position
  costs = np.sum(mat, 0).astype(int).tolist()

  best_cost = min(costs)
  goal_position = costs.index(best_cost) + l
  return goal_position, best_cost

def exp_cost(positions, goal):
  fuel = lambda dist: sum([ i for i in range(1, dist+1) ])
  return sum([fuel(abs(p - goal)) for p in positions])

goal, answer_b = exp_goal(positions)

print(f"Part 2: {answer_b}")
print(aoc.post_result(day=DAY, part=2, value=answer_b, year=2021))
