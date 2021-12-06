#!/usr/bin/env python3

import itertools

def make_pairs(l):
  return itertools.combinations(l, 2)

def sums(pairs):
  return set([ x+y for x,y in pairs])

inputs = []
with open("9.txt", "r") as f:
  inputs = [ int(l.strip()) for l in f.readlines() ]


winlen = 25

invalid_number = 0
for i in range(winlen+1, len(inputs)):
  num = inputs[i]
  window = inputs[i-winlen:i]
  if num not in sums(make_pairs(window)):
    invalid_number = num
    break

print("Part A: {}".format(invalid_number))

# Part B: Find a sequence in the input which sums up to that number
sequence = []
for start in range(len(inputs)):
  for count in range(2,len(inputs) - start):
    win = inputs[start:start+count]
    total = sum(win)

    if (total > invalid_number): break

    if (total == invalid_number):
      sequence = win
      break
  if sequence != []: break

print("Part B: {}".format(min(sequence) + max(sequence)))
