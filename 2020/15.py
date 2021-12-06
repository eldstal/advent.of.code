#!/usr/bin/env python3

def elfgame(starter, steps):
  recent = { v:i for i,v in enumerate(starter) }

  key = starter[-1]
  for i in range(len(starter),steps):
    if (key in recent):
      age = i - 1 - recent[key]
    else:
      age = 0

    recent[key] = i-1
    key = age

  return key


if False:
  assert(elfgame([0,3,6], 2020) == 436)
  assert(elfgame([1,3,2], 2020) == 1)
  assert(elfgame([2,1,3], 2020) == 10)
  assert(elfgame([1,2,3], 2020) == 27)
  assert(elfgame([3,2,1], 2020) == 438)
  assert(elfgame([3,1,2], 2020) == 1836)

print("Part A: {}".format(elfgame([20,9,11,0,1,2], 2020)[-1]))


if False:
  assert(elfgame([0,3,6], 30000000) == 175594)
  assert(elfgame([1,3,2], 30000000) == 2578)
  assert(elfgame([2,1,3], 30000000) == 3544142)
  assert(elfgame([1,2,3], 30000000) == 261214)
  assert(elfgame([3,2,1], 30000000) == 18)
  assert(elfgame([3,1,2], 30000000) == 362)

print("Part B: {}".format(elfgame([20,9,11,0,1,2], 30000000)))
#print(elfgame([0,3,6], 30000000))
#print(elfgame([0,3,6], 30000000))
