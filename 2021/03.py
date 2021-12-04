import aoc

DAY=3

#_, lines = aoc.get_input(DAY)
_, lines = aoc.get_test_input(DAY)

# Test data
#lines = [ "00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010" ]

BITS = len(lines[0])
nums = [ int(l, 2) for l in lines ]

def get_gamma_epsilon(numbers):

  set_bit_counts = [ 0 for pos in range(BITS) ]

  for n in numbers:
    for pos in range(BITS):
      if n & (0x1 << pos): set_bit_counts[pos] += 1

  gamma = 0
  for pos in range(BITS-1, -1, -1):
    if set_bit_counts[pos] >= (len(numbers) - set_bit_counts[pos]):
      gamma = (gamma << 1) | 0x1
    else:
      gamma = (gamma << 1) | 0x0

  # epsilon is always the inverse of gamma
  epsilon = gamma ^ ((0x1 << BITS) - 1)

  return gamma, epsilon


gamma, epsilon = get_gamma_epsilon(nums)
print(f"Gamma: {gamma:x}  Epsilon: {epsilon:x}")

answer_a = gamma * epsilon

print(f"Part 1: {answer_a}")
#print(aoc.post_result(day=DAY, part=1, value=answer_a, year=2021))


def is_oxygen(num, pos, gamma):
  return (((num ^ gamma) >> pos) & 0x1) ^ 0x1

def is_co2(num, pos, epsilon):
  return (((num ^ epsilon) >> pos) & 0x1) ^ 0x1

o2 = [ n for n in nums ]
co2 = [ n for n in nums ]

for pos in range(BITS-1, -1, -1):
  if len(o2) > 1:
    gamma_o2, epsilon_o2 = get_gamma_epsilon(o2)
    o2 = [ num for num in o2 if is_oxygen(num, pos, gamma_o2) ]

  if len(co2) > 1:
    gamma_co2, epsilon_co2 = get_gamma_epsilon(co2)
    co2 = [ num for num in co2 if is_co2(num, pos, epsilon_co2) ]

print(o2)
print(co2)

answer_b = o2[0] * co2[0]

print(f"Part 2: {answer_b}")
#print(aoc.post_result(day=DAY, part=2, value=answer_b, year=2021))
