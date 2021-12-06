#!/usr/bin/env python3

import re

# The input is key:value sometimes split by newline, sometimes by space
# Groups are delimited by \n\n
#
# Validate that groups contain all expected fields



# Returns a list of missing fields
def missing_fields(entry, fields):
  missing = []
  for f,_ in fields.items():
    tag = "{}:".format(f)
    if tag not in entry:
      missing += [f]
  return missing

# Returns a list of missing or invalid fields
def invalid_fields(entry, fields):
  failed = []

  for f,valid in fields.items():
    expr = ".*{}:(?P<value>[^ ]+).*".format(f)
    m = re.match(expr, entry)

    if m is None:
      failed += [f]   # Missing field
      continue

    value = m.group("value")

    if not valid(value):
      failed += [f]   # Invalid value
      #print("Invalid {} = {}".format(f, value))

  return failed

groups = []
with open("4.txt", "r") as f:
  groups = f.read().split("\n\n")

groups = [ g.replace("\n", " ") for g in groups ]

in_range = lambda x,l,u: x <= u and x >= l
inches = lambda s: re.fullmatch("[0-9]+in",s) is not None and in_range(int(s[:-2]), 59, 76)
centis = lambda s: re.fullmatch("[0-9]+cm",s) is not None and in_range(int(s[:-2]), 150, 193)

fields = {
           "byr" : lambda s: len(s) == 4 and in_range(int(s), 1920, 2002),
           "iyr" : lambda s: len(s) == 4 and in_range(int(s), 2010, 2020),
           "eyr" : lambda s: len(s) == 4 and in_range(int(s), 2020, 2030),
           "hgt" : lambda s: inches(s) or centis(s),
           "hcl" : lambda s: re.fullmatch("#[0-9a-fA-F]{6}", s) is not None,
           "ecl" : lambda s: s in [ "amb", "blu", "brn", "gry", "grn", "hzl", "oth" ],
           "pid" : lambda s: re.fullmatch("[0-9]{9}", s),
           #"cid" : lambda s: True    # Don't care, hax
         }

n_valid_a = 0
n_valid_b = 0
for g in groups:
  m = missing_fields(g, fields)
  if len(m) == 0: n_valid_a += 1

  i = invalid_fields(g, fields)
  if len(i) == 0: n_valid_b += 1

print("Part a: {}".format(n_valid_a))
print("Part b: {}".format(n_valid_b))


