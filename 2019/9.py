#!/usr/bin/env python3

from intcode import load_prog, run_prog

test_quine = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99] 

state = load_prog("9.txt")
state.mem = list(test_quine)
run_prog(state)

print("Test Quine in : {}".format(test_quine))
print("Test Quine out: {}".format(state.stdout))



state = load_prog("9.txt")
state.stdin = [1]
run_prog(state)

print("Part A: {}".format(state.stdout))


state = load_prog("9.txt")
state.stdin = [2]
run_prog(state)

print("Part B: {}".format(state.stdout))

