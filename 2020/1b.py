#!/usr/bin/env python3

# Find the two numbers which sum to 2020 and multiply them

def solve(numbers):
  if len(numbers) < 2: return 0,0,0

  i = numbers[0]
  for j in numbers[1:]:
    for k in numbers[2:]:
      if i + j + k == 2020:
        return i,j,k

  return solve(numbers[1:])

inputs = []
with open("1.txt", "r") as f:
  inputs = list([ int(l) for l in f.readlines() ])

print(len(inputs))

i,j,k = solve(inputs)

print("{} + {} + {} = {}".format(i, j, k, i+j+k))
print("{} * {} * {} = {}".format(i, j, k, i*j*k))
