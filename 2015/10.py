#!/usr/bin/env python3

import aoc
import re

#_,lines = aoc.get_input(9)
indata = "1113122113"

PREFIX = re.compile(r"^(.)\1*")

# returns (remainder, length, value)
def _eat_sequence(text):
  m = PREFIX.match(text)
  v = text[0]
  l = len(m.group(0))
  remainder = text[l:]

  return remainder, l, v

def eat_sequence(text):
  v = text[0]
  l = 1
  for i in range(1,len(text)-1):
    if text[l] != v: break
    l += 1

  remainder = text[l:]
  return remainder, l, v


def rle(text):
  encoded = ""
  while len(text) > 0:
    text,l,v = eat_sequence(text)
    encoded += f"{l}{v}"

  return encoded


print(rle("111221"))

text = rle(indata)

for i in range(1,40):
  text = rle(text)

text_a = text
print(f"Part 1: {len(text_a)} characters")

text_b = text

for i in range(10):
  text_b = rle(text_b)

print(f"Part 1: {len(text_b)} characters")



