#!/usr/bin/env python3

# The input is a vertical slice of the map
# . is an empty space
# # is a tree
#
# Count the number of trees you would hit if you kept going right 3 and down 1
# until the map ends

dx = 3
dy = 1


inputs = []
with open("3.txt", "r") as f:
  inputs = list([l.strip() for l in f.readlines()])

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

print(trees)
