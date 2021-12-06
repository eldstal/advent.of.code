#!/usr/bin/env python3
import re
import numpy as np

# Returns (name,lambda) where lambda 
def line_as_rule(text):
  m = re.match("^(?P<name>[^:]+): (?P<l1>[0-9]+)-(?P<u1>[0-9]+) or (?P<l2>[0-9]+)-(?P<u2>[0-9]+)$", text)
  assert(m is not None)

  name = m.group("name")
  limits = list(map(int, map(m.group, [ "l1", "u1", "l2", "u2" ])))

  func = lambda n: (limits[0] <= n and n <= limits[1]) or (limits[2] <= n and n <= limits[3])
  return name,func

rules = []
my_ticket = []
other_tickets = []

with open("16.txt", "r") as f:
  lines = [ l.strip() for l in f.readlines() ]
  l = 0
  for l in range(l,len(lines)):
    if lines[l] == "": continue
    if "your ticket" in lines[l]: break
    rules += [ line_as_rule(lines[l]) ]

  my_ticket = list(map(int, lines[l+1].split(",")))
  l += 3

  for l in range(l+1,len(lines)):
    other_tickets += [ list(map(int, lines[l].split(","))) ]


def sum_invalid_fields(ticket, rules):
  count = 0
  total = 0
  for num in ticket:
    matches = sum([ r(num) for _,r in rules ])
    if matches == 0:
      total += num
      count += 1
  return count,total

num_invalid = sum([ sum_invalid_fields(t, rules)[1] for t in other_tickets ])
print("Part A: {}".format(num_invalid))


valid_tickets = list(filter(lambda t: sum_invalid_fields(t, rules)[0] == 0, other_tickets))
print("Part B: {} valid tickets".format(len(valid_tickets)))

# A row is a named rule, a column is a ticket field
n_fields = len(my_ticket)

T = np.array(valid_tickets)
A = np.ndarray((len(rules), n_fields))


for r,rule in enumerate(rules):
  name, func = rule
  A[r, :] = [ all(map(func, T[:,idx])) for idx in range(n_fields) ]

# Finds an only-one-option row or column
# Returns new_A,rule_no,field_no
def squeeze_one(A):
  rules,fields = A.shape

  for r in range(rules):
    if np.sum(A[r,:]) == 1:
      f = np.nonzero(A[r,:])[0][0]
      A[r,:] = 0
      A[:,f] = 0
      return A,r,f

  for f in range(fields):
    if np.sum(A[:,f]) == 1:
      r = np.nonzero(A[:,f])[0][0]
      A[:,f] = 0
      A[r,:] = 0
      return A,r,f

  return A,-1,-1


known_pos = {}
while True:
  A,r,f = squeeze_one(A)
  if (r == -1): break
  known_pos[rules[r][0]] = f

assert(np.all(A == 0))
print(known_pos)

prod = 1
for name,pos in known_pos.items():
  if "departure" in name:
    print("Adding {} from pos {}".format(name, pos))
    prod *= my_ticket[pos]

print("Part B: {}".format(prod))
