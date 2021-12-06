#!/usr/bin/env python3

from intcode import load_prog, run_prog

state = load_prog("5.txt")
state.stdin = [1]
run_prog(state)

print("Part A: {}".format(state.stdout))



state = load_prog("5.txt")
state.stdin = [5]
run_prog(state)

print("Part B: {}".format(state.stdout))


