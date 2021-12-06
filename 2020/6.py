#!/usr/bin/env python3
import string

def unique_letters(group):
  letters = group.replace("\n","")
  return set([a for a in letters])

def common_letters(group):
  people = group.strip().split("\n")

  # Each person's answers
  answers = [ set(p) for p in people ]

  letters = answers[0].intersection(*answers)
  return letters

groups = []
with open("6.txt", "r") as f:
  groups = f.read().split("\n\n")


total_a = sum([len(unique_letters(g)) for g in groups])
print("Part A: {}".format(total_a))

total_b = sum([len(common_letters(g)) for g in groups])
print("Part B: {}".format(total_b))
