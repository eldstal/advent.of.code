#!/usr/bin/env python3

from intcode import load_prog, run_prog

def attempt(noun, verb):
  state = load_prog("2.txt")

  # Part A: Patch the program and execute.
  state.mem[1] = noun
  state.mem[2] = verb

  run_prog(state)

  return state.mem[0]


# Part A: Patch the program and execute.
print("Part A: {}".format(attempt(12, 2)))



# Part B: Find the inputs which give an output of 19690720
target = 19690720
for verb in range(100):
  for noun in range(100):
    if (attempt(noun, verb) == target):
      print("Part B: 100 * {} + {} == {}".format(noun, verb, 100*noun + verb))
