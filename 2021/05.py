import aoc
import numpy as np
import re

DAY=5

_, lines = aoc.get_input(DAY)
#_, lines = aoc.get_test_input(DAY)

PARSE = re.compile("(?P<x1>[0-9]+),(?P<y1>[0-9]+) -> (?P<x2>[0-9]+),(?P<y2>[0-9]+)")

segments = []
for l in lines:
  m = PARSE.match(l)
  if m is None: raise RuntimeError(l)

  seg = ( int(m.group("x1")),
          int(m.group("y1")),
          int(m.group("x2")),
          int(m.group("y2"))
        )
  segments.append(seg)


def area_dims(segments):
  w = 0
  h = 0
  for x1,y1,x2,y2 in segments:
    w = max([w, x1, x2])
    h = max([h, y1, y2])

  return h+1,w+1

def line_points(seg):
  x1,y1,x2,y2 = seg
  dx = x2 - x1
  dy = y2 - y1
  steps = max(abs(dx), abs(dy))
  sx = dx / steps
  sy = dy / steps
  pts = []
  for i in range(steps+1):
    x = int(x1 + i*sx)
    y = int(y1 + i*sy)
    pts.append((x,y))
  return pts

def paint_field(segments):
  dims = area_dims(segments)
  field = np.full(dims, fill_value=0, dtype=int)
  for seg in segments:
    for x,y in line_points(seg):
      field[y,x] += 1

  return field



def is_hv(seg):
  x1,y1,x2,y2 = seg
  return x1==x2 or y1==y2

hv_segments = list(filter(is_hv, segments))
field = paint_field(hv_segments)
answer_a = np.sum(field > 1)

print(f"Part 1: {answer_a}")
#print(aoc.post_result(day=DAY, part=1, value=answer_a, year=2021))


field = paint_field(segments)
answer_b = np.sum(field > 1)

print(f"Part 2: {answer_b}")
#print(aoc.post_result(day=DAY, part=2, value=answer_b, year=2021))
