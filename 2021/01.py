import aoc

_, lines = aoc.get_input(1)

def count_increments(values):
  delta = [ values[i] - values[i-1] for i in range(1, len(values)) ]
  increasing = [ d > 0 for d in delta ]
  inc_count = sum(increasing)

  return inc_count

depth = [ int(l) for l in lines ]
inc_count = count_increments(depth)

print(f"Part 1: number of increments: {inc_count}")
#print(aoc.post_result(day=1, part=1, value=inc_count, year=2021))

windows = [ sum(depth[i-1:i+2]) for i in range(1, len(depth)-1) ]
inc_count_win = count_increments(windows)

print(f"Part 2: number of sliding-window increments: {inc_count_win}")
#print(aoc.post_result(day=1, part=2, value=inc_count_win, year=2021))
