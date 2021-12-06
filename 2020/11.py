#!/usr/bin/env python3

import numpy as np

def rule_A(seats, r, c):

  tile = seats[r,c]
  if (tile == -1): return tile

  area = seats[r-1:r+2,c-1:c+2].copy()

  count = np.sum(area == 1) - tile

  if count == 0:
    return 1    # Occupy this seat!
  elif count >= 4:
    return 0    # Get up and leave
  else:
    return tile # No change

def ray(seats, r, c, delta):
  dy,dx = delta
  my,mx = seats.shape

  x = c + dx
  y = r + dy

  los = []
  while ((x > 0 and x < mx) and
         (y > 0 and y < my)):
    los += [seats[y,x]]
    y+=dy
    x+=dx

  return los

# Returns 1 if an occupied seat is seen in this direction
# 0 otherwise
def first_seat(seats, r, c, delta):

  los = ray(seats, r, c, delta)

  #print("{},{} dir {}  los {}".format(r,c,delta, los))
  # No filled seat seen
  if 1 not in los: return 0

  # Only a filled seat seen
  if 0 not in los: return 1

  # Nearest seat is full
  if los.index(1) < los.index(0): return 1

  # Nearest seat is empty
  return 0


def rule_B(seats, r, c):
  tile = seats[r,c]
  if (tile == -1): return tile

  directions = [ (-1, 0),
                 (-1, 1),
                 (0, 1),
                 (1, 1),
                 (1, 0),
                 (1, -1),
                 (0, -1),
                 (-1, -1) ]

  hits = sum([ first_seat(seats, r, c, d) for d in directions])

  if hits == 0:
    return 1    # Occupy this seat
  elif hits >= 5:
    return 0    # Get up and leave
  else:
    return tile # No change

# Seats matrix should be padded, edges are ignored.
# Returns (seats,stable)
def tick(seats, rule=rule_A):
  ret = seats.copy()
  rows,cols = seats.shape
  for r in range(1,rows-1):
    for c in range(1,cols-1):
      ret[r,c] = rule(seats, r, c)

  return ret,np.all(ret == seats)

tilemap = { ".":-1, "L":0, "#":1 }

def load_seats():
  inputs = []
  with open("11.txt", "r") as f:
    for l in f.readlines():
      inputs += [[ tilemap[c] for c in l.strip() ]]

  # Convert to a numpy matrix for magic
  seats = np.array(inputs)
  seats = np.pad(seats, [(1,1), (1,1)], constant_values=-1)

  return seats


seats = load_seats()
done = False
while not done:
  seats,done = tick(seats, rule_A)

print("Part A: {}".format(np.sum(seats == 1)))

seats = load_seats()
done = False
while not done:
  seats,done = tick(seats, rule_B)

print("Part B: {}".format(np.sum(seats == 1)))
