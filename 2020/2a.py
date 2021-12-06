#!/usr/bin/env python3

import re

# An input like
# 4-8 g: asdf12fnadslknjasdclkjn
#
# means "The password policy is somewhere between 4 and 8 g:s must be in the password.
#
# How many input lines are valid according to their attached rule?

def validate(entry):
  matches = re.findall(entry["char"], entry["pass"])
  if (len(matches) < entry["min"]): return False
  if (len(matches) > entry["max"]): return False
  return True

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
