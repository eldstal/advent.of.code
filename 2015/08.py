#!/usr/bin/env python3

import aoc
import re

_,lines = aoc.get_input(8)

def unescape(text):

  squeezed_text = bytes(text, "utf-8").decode("unicode_escape")

  # Remove the quote wrapping
  return squeezed_text[1:-1]

a_code = 0
a_mem = 0
for dirty in lines:
  clean = unescape(dirty)
  a_code += len(dirty)
  a_mem += len(clean)

print(f"Part 1: {a_code}-{a_mem} = {a_code-a_mem} characters")


def escape(text):
  text = re.sub(r"(\"|\\)", r"\\\1", text)
  return "\"" + text + "\""

b_code = 0
b_recode = 0
for dirty in lines:
  dirtier = escape(dirty)
  b_code += len(dirty)
  b_recode += len(dirtier)
  #print(f"{dirty} -> {dirtier}")


print(f"Part 2: {b_recode}-{b_code} = {b_recode-b_code} characters")

