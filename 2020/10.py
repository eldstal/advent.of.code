#!/usr/bin/env python3


def is_valid(adapter_set, device_rating):

  # Invalid last adapter
  if (device_rating - 3) not in adapter_set: return False

  prev = 0
  for adapter in sorted(adapter_set):
    if adapter > prev + 3: return False
    prev = adapter

  return True

# Pass in a sorted list
# Returns the number of valid sub-tails
def number_of_chains(adapters, head=0, memo={}):
  if len(adapters) == 0: return 1

  if head in memo: return memo[head]

  ret = 0
  for i in range(len(adapters)):
    v = adapters[i]

    # Can't continue with this value
    if (v > (head + 3)): break

    # Yes we can!
    ret += number_of_chains(adapters[i+1:], v)

  #print(ret)

  memo[head] = ret
  return ret

inputs = []
with open("10.txt", "r") as f:
  inputs = [ int(l.strip()) for l in f.readlines() ]

# Connection order
inputs = sorted(inputs)

device_rating = max(inputs) + 3
print("Device rating: {}".format(device_rating))

ones = 0
threes = 1    # Device's rating is max adapter + 3

prev = 0
for rating in inputs:
  diff = rating - prev
  prev = rating
  if diff == 1: ones += 1
  if diff == 3: threes += 1

print("Part A: {}".format(ones*threes))


combos = number_of_chains(inputs)

print("Part B: {}".format(combos))

