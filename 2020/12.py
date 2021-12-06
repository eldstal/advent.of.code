#!/usr/bin/env python3

from math import sin, cos, atan, radians, sqrt

inputs = []
with open("12.txt", "r") as f:
  for l in f.readlines():
    l = l.strip()
    inputs += [ ( l[0], int(l[1:]) ) ]



# East
heading = 0
n = 0
e = 0

for cmd,num in inputs:
  if cmd == "L":
    heading += num
  if cmd == "R":
    heading -= num
  if cmd == "N":
    n += num
  if cmd == "S":
    n -= num
  if cmd == "E":
    e += num
  if cmd == "W":
    e -= num
  if cmd == "F":
    e += num * int(cos(radians(heading)))
    n += num * int(sin(radians(heading)))

print("Part A: {}".format(abs(n) + abs(e)))



def rot(x, y, deg):
  deg = int(deg) % 360

  if (deg == 90): return -y,x
  if (deg == 180): return -x,-y
  if (deg == 270): return y,-x
  return x,y

# Ship
e = 0
n = 0

# Relative to the ship
wn = 1
we = 10

for cmd,num in inputs:
  if cmd == "L":
    we, wn = rot(we, wn, num)
  if cmd == "R":
    we, wn = rot(we, wn, -num)
  if cmd == "N":
    wn += num
  if cmd == "S":
    wn -= num
  if cmd == "E":
    we += num
  if cmd == "W":
    we -= num
  if cmd == "F":
    e += num * we
    n += num * wn

print("Part B: {}".format(abs(n) + abs(e)))

