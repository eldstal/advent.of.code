#!/usr/bin/env python3

def direction(cardinal, dist):
  return { "U": ( 0,   -dist),
           "D": ( 0,    dist),
           "R": ( dist, 0),
           "L": (-dist, 0)
         }[cardinal]

def paint(seq):
  x = 0
  y = 0

  tiles = set()
  for step in seq:
    dist = int(step[1:])
    dx,dy = direction(step[0], dist)

    if dx != 0:
      for mx in range(1,dx+1):
        tiles.add((x+mx, y))

    if dy != 0:
      for my in range(1,dy+1):
        tiles.add((x+dx, y))

    x += dx
    y += dy

  return tiles

def manhattan(tile):
  return abs(tile[0]) + abs(tile[1])

inputs = []
with open("3_manual.txt", "r") as f:
  inputs = [ l.strip().split(",") for l in f.readlines() ]

a = paint(inputs[0])
b = paint(inputs[1])


print(sorted(a, key=manhattan))
print(sorted(b, key=manhattan))

intersects = a.intersection(b)

print(intersects)
print([manhattan(t) for t in intersects])
print(min([manhattan(t) for t in intersects]))
