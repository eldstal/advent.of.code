#!/usr/bin/env python3


inputs = []
with open("1.txt", "r") as f:
  inputs = [ int(l.strip()) for l in f.readlines() ]

cost = lambda m: int(m/3) - 2

cargo = sum([cost(m) for m in inputs])

print("Part a: {}".format(cargo))

fuel = 0
step = cargo
while step > 0:
  fuel += step
  step = cost(step)
  print(step)

print("Part b (from total A): {}".format(fuel))



fuel = 0
for module in inputs:
  step = cost(module)
  while step > 0:
    fuel += step
    step = cost(step)

print("Part b (individuals): {}".format(fuel))
