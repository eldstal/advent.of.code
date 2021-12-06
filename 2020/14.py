#!/usr/bin/env python3
import re
import numpy as np

def letter_to_bits(string, letter):
  as_bytes = np.packbits([ c == letter for c in string ])
  as_num = int.from_bytes(as_bytes, byteorder='big', signed=False)

  # Gets padded with least-significant bits for some fucking reason
  return as_num >> (len(string) % 8)

# Returns (exes,ones,zeroes) from that icky string
def make_mask(mask_string):
  exes = letter_to_bits(mask_string, "X")
  ones = letter_to_bits(mask_string, "1")
  zeroes = letter_to_bits(mask_string, "0")
  return exes,ones,zeroes

# Provide a mask from make_mask and all will be well
def apply_mask_data(value,mask):
  exes, ones, _ = mask
  return value & exes | ones

# Concretify all the floating bits
def permute_addr(addr, exes, pos=0):
  if (exes >> pos) == 0: return [addr]

  bitmask = 1 << pos
  if exes & bitmask != 0:
    one = addr | bitmask
    return permute_addr(addr, exes, pos+1) + permute_addr(one, exes, pos+1)
  else:
    return permute_addr(addr, exes, pos+1)

# Returns a list of addresses, since the X bits are floating
def apply_mask_addr(addr, mask):
  exes, ones, zeroes = mask
  known_bits = addr & zeroes | ones

  permutations = permute_addr(known_bits, exes)

  return permutations

inputs = []
with open("14.txt", "r") as f:
  inputs = [ l.strip() for l in f.readlines() ]

mem_A = {}
mem_B = {}
mask = make_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
for cmd in inputs:
  if "mask" in cmd:
    mask_string = cmd.split("= ")[1]
    mask = make_mask(mask_string)

  else:
    m = re.match("^mem\[(?P<addr>[0-9]+)\] = (?P<value>[0-9]+)$", cmd)
    addr_A = int(m.group("addr"))
    value_B = int(m.group("value"))

    addr_B = apply_mask_addr(addr_A, mask)
    value_A = apply_mask_data(value_B, mask)

    mem_A[addr_A] = value_A

    for a in addr_B:
      mem_B[a] = value_B

total_A = sum(mem_A.values())
print("Part A: {}".format(total_A))

total_B = sum(mem_B.values())
print("Part B: {}".format(total_B))
