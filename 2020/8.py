#!/usr/bin/env python3

from vm import VM


# Part A: Where do we loop?
vm = VM()
vm.load("8.txt")

while vm.step() == 1:
  pass

print("Part A: {}".format(vm.acc))


#n_instructions = len(vm.prog)
suspicious_ips = vm.trace

vm = VM()
vm.load("8.txt")

# Modify one instruction at a time
for i in suspicious_ips:
  if (vm.prog[i][0] == "jmp"):
    vm.prog[i][0] = "nop"
  elif (vm.prog[i][0] == "nop"):
    vm.prog[i][0] = "jmp"
  else:
    # Try another instruction
    continue

  while vm.step() == 1: pass

  if (vm.status() == 0):
    print("Part B: {} (modified instruction {})".format(vm.acc, i))
    break

  # That wasn't it, try again
  vm.reset()
  vm.load("8.txt")

