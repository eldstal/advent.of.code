import aoc

DAY=6

_, lines = aoc.get_input(DAY)
#_, lines = aoc.get_test_input(DAY)


# The state is a list of exactly 9 integers
# Each is a count of fishies with the same internal state
def run_generation_O1(state):
  # Time passes
  n_births = state[0]
  state = state[1:] + [0]

  # New fishies are born
  state[8] += n_births

  # Parent fishies are reset
  state[6] += n_births

  return state

def run_O1(lines, generations):
  start_fishies = list(map(int, lines[0].split(",")))
  start_state = [ start_fishies.count(n) for n in range(9) ]

  state = start_state
  for n in range(generations):
    state = run_generation_O1(state)

  return sum(state)

answer_a = run_O1(lines, 80)

print(f"Part 1: {answer_a}")
#print(aoc.post_result(day=DAY, part=1, value=answer_a, year=2021))


answer_b = run_O1(lines, 256)

print(f"Part 2: {answer_b}")
#print(aoc.post_result(day=DAY, part=2, value=answer_b, year=2021))
