import aoc
import re

_, lines = aoc.get_input(2)

PARSE=re.compile("(?P<dir>forward|down|up) (?P<dist>[0-9]+)")

instructions = [ ]
for l in lines:
  m = PARSE.match(l)
  if m is None: raise RuntimeError(l)

  s = ( m.group("dir"), int(m.group("dist")) )
  instructions.append(s)

x = 0
y = 0

for direction,dist in instructions:
  if direction == "forward": x+= dist
  elif direction == "up": y-= dist
  elif direction == "down": y+= dist
  else: raise RuntimeError(direction)

answer_a = x * y

print(f"Part 1: {answer_a}")
#print(aoc.post_result(day=2, part=1, value=answer_a, year=2021))

x = 0
y = 0
aim = 0

for cmd,dist in instructions:
  if cmd == "forward":
    x += dist
    y += aim * dist
  elif cmd == "up":
    aim -= dist
  elif cmd == "down":
    aim += dist
  else: raise RuntimeError(direction)

answer_b = x * y

print(f"Part 2: {x} * {y} = {answer_b}")
#print(aoc.post_result(day=2, part=2, value=answer_b, year=2021))
