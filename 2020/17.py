#!/usr/bin/env python3

import numpy as np

def react_3d(area):
  self = area[1,1,1]
  activity = np.sum(area) - self

  if not self and activity == 3: return 1
  if self and activity == 2: return 1
  if self and activity == 3: return 1

  return 0

def tick_3d(field):
  A = field.copy()
  d,h,w = field.shape
  # Check everything except the holy zeroed shell
  for z in range(1,d-1):
    for y in range(1,h-1):
      for x in range(1,w-1):
        area = field[z-1:z+2, y-1:y+2, x-1:x+2]
        A[z,y,x] = react_3d(area)

  # Expand for the future if anything is approaching the zero shell
  shell = np.sum(A) - np.sum(A[2:-2, 2:-2, 2:-2])
  if shell != 0:
    A = np.pad(A, [ (1,1), (1,1), (1,1) ], constant_values=0)
  return A



inputs = []
with open("17.txt", "r") as f:
  inputs = [ [ c == "#" for c in l.strip() ] for l in f.readlines() ]

floor = np.array(inputs)
h,w = floor.shape

# 2-wide Zeroed shell around the play field.
# The outermost shell will always be zero, for simplicity
# The innermost is expansion space. The gol can spread there.
field = np.ndarray((5,h+4,w+4), dtype=int)
field[:,:,:] = 0
field[2,2:-2,2:-2] = floor

#print(field)

for frame in range(6):
  field = tick_3d(field)

#print(field)
print("Part A: {} (play field is {})".format(np.sum(field), field.shape))




def react_4d(area):
  self = area[1,1,1,1]
  activity = np.sum(area) - self

  if not self and activity == 3: return 1
  if self and activity == 2: return 1
  if self and activity == 3: return 1

  return 0

def tick_4d(field):
  A = field.copy()
  S,D,H,W = field.shape
  # Check everything except the holy zeroed shell
  for w in range(1,S-1):
    for z in range(1,D-1):
      for y in range(1,H-1):
        for x in range(1,W-1):
          area = field[w-1:w+2, z-1:z+2, y-1:y+2, x-1:x+2]
          A[w,z,y,x] = react_4d(area)

  # Expand for the future if anything is approaching the zero shell
  shell = np.sum(A) - np.sum(A[2:-2:, 2:-2, 2:-2, 2:-2])
  if shell != 0:
    A = np.pad(A, [ (1,1), (1,1), (1,1), (1,1) ], constant_values=0)
  return A

inputs = []
with open("17.txt", "r") as f:
  inputs = [ [ c == "#" for c in l.strip() ] for l in f.readlines() ]

floor = np.array(inputs)
h,w = floor.shape

# 2-wide Zeroed shell around the play field.
# The outermost shell will always be zero, for simplicity
# The innermost is expansion space. The gol can spread there.
field = np.ndarray((5, 5,h+4,w+4), dtype=int)
field[:,:,:,:] = 0
field[2, 2, 2:-2, 2:-2] = floor

for frame in range(6):
  field = tick_4d(field)

print("Part B: {} (play field is {})".format(np.sum(field), field.shape))

