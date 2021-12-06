#!/usr/bin/env python3

import re

# An input like
# 4-8 g: asdf12fnadslknjasdclkjn
#
# means exactly one of positions 4 and 8 must be "g"
# careful: it's one-indexed!
#
# How many input lines are valid according to their attached rule?

def validate(entry):
  if (len(entry["pass"]) < entry["min"]): return False
  if (len(entry["pass"]) < entry["max"]): return False

  pos1 = entry["pass"][entry["min"] - 1] == entry["char"]
  pos2 = entry["pass"][entry["max"] - 1] == entry["char"]

  return pos1 ^ pos2

FORMAT = re.compile('^(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<char>[a-z]): (?P<pass>.*)$')

inputs = []
with open("2.txt", "r") as f:
  for l in f.readlines():
    m = re.match(FORMAT, l)
    entry = {
              "min": int(m.group("min")),
              "max": int(m.group("max")),
              "char": m.group("char"),
              "pass": m.group("pass")
            }
    inputs += [entry]


ok = 0
for e in inputs:
  if validate(e): ok += 1

print(ok)
