#!/usr/bin/env python3

import re

rules = {}
messages = []
with open("19.txt", "r") as f:
  sections = f.read().split("\n\n")
  messages = [ l.strip() for l in sections[1].split("\n") ]

  for l in sections[0].split("\n"):
    parts = l.strip().split(": ")
    num = int(parts[0])
    expr = parts[1]
    rules[num] = expr


def rule_to_regex(expr):
  if "\"" in expr:
    return expr[1]   # Single character

  if " | " in expr:
    l = expr.split(" | ")[0]
    r = expr.split(" | ")[1]
    return "({})|({})".format(rule_to_regex(l), rule_to_regex(r))

  if " " in expr:
    sub = expr.split(" ")
    regex = ""
    for s in sub:
      regex += "({})".format(regex_for_num(int(s)))
    return regex

  return regex_for_num(int(expr))


# Fully resolved regexes, keyed by their number
memo = {}
def regex_for_num(num):
  if num in memo: return memo[num]

  expr = rules[num]
  regex = rule_to_regex(expr)
  memo[num] = regex
  return regex



count = 0
regex = "^" + regex_for_num(0) + "$"
for m in messages:
  if re.search(regex, m): count+=1

print("Part A: {}".format(count))



memo = {}

# Regex hacks because I'm too lazy for a general implementation
# 8 = (42)+
rules[8] = "42 | 42 8"
memo[8] = "(" + regex_for_num(42) + ")+"


# 11 = (n * 42)(n * 31)
rules[11] = "42 31 | 42 11 31"
lump = ""
options = []
for len in range(4):
  lump = "(" + regex_for_num(42) +")" + lump + "(" + regex_for_num(31) + ")"
  options += [lump]
memo[11] = "|".join(options)



count = 0
regex = "^" + regex_for_num(0) + "$"
for m in messages:
  if re.search(regex, m): count+=1

print("Part B: {}".format(count))
