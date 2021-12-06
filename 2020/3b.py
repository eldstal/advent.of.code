#!/usr/bin/env python3

# The input is a vertical slice of the map
# . is an empty space
# # is a tree
#
# Same as 3a, but for a variety of slopes

def ouch(inputs, dx, dy):

  h = len(inputs)
  w = len(inputs[0])

  y = dy
  x = dx
  trees = 0

  while y < h:

    tile = inputs[y][x % w]
    if (tile == "#"): trees += 1

    y += dy
    x += dx

  return trees


inputs = []
with open("3_baot.txt", "r") as f:
  inputs = list([l.strip() for l in f.readlines()])


slopes = [
  (1,1),
  (3,1),
  (5,1),
  (7,1),
  (1,2),
]

product = 1
for dx, dy in slopes:
  factor = ouch(inputs, dx, dy)
  print(factor)
  product *= factor

print(product)
