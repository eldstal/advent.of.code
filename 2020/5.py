#!/usr/bin/env python3

import re

# The input is key:value sometimes split by newline, sometimes by space
# Groups are delimited by \n\n
#
# Validate that groups contain all expected fields

def parse_pass_(code):
  row = code[:7].replace("F", "0").replace("B", "1")
  seat = code[7:].replace("L", "0").replace("R", "1")
  place = (int(row, 2), int(seat, 2))
  return place

# Returns a numeric seat
def parse_pass(code):
  place = code.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
  seatid = int(place, 2)
  row = seatid >> 3
  col = seatid & 0x3
  return (seatid, row, col)

inputs = []
with open("5.txt", "r") as f:
  inputs = [ l.strip() for l in f.readlines() ]

free_ids = set(range(1024))
taken_ids = set()

for code in inputs:
  seatid,row,col = parse_pass(code)
  free_ids.discard(seatid)
  taken_ids.add(seatid)

print("Part a: {}".format(max(taken_ids)))

my_id = 0
for t in taken_ids:
  if (t-2 in taken_ids and (t-1) in free_ids):
    my_id = t-1
    break

print("Part b: {}".format(my_id))

