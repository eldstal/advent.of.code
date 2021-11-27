#!/usr/bin/env python3

import aoc
import re
import networkx as nx
import itertools

_,lines = aoc.get_input(9)


PARSE = re.compile(r"^(?P<src>\w+) to (?P<dst>\w+) = (?P<dist>[0-9]+)$")

G = nx.Graph()

places = {}
for l in lines:
  m = PARSE.match(l)
  if m is None:
    raise RuntimeError(l)

  G.add_edge( m.group("src"), m.group("dst"), weight=int(m.group("dist")))
  places[m.group("src")] = True
  places[m.group("dst")] = True

cities = places.keys()
paths = itertools.permutations(cities, len(cities))

shortest = -1
longest = -1
for path in paths:
  d = nx.classes.function.path_weight(G, path, weight="weight")
  if shortest < 0 or d < shortest:
    shortest = d
  if longest < 0 or d > longest:
    longest = d



print(f"Part 1: Shortest path is {shortest}")
print(f"Part 2: Longest path is {longest}")


