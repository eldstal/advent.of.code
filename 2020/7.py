#!/usr/bin/env python3

import re
import math
import networkx as nx

# Returns list of (src, dst, weight)
def text_to_edges(line):
  edges = []

  src_match = re.match("^(?P<src>[^ ]+ [^ ]+) bags contain.*", line)
  src = src_match.group("src")

  dst_match = re.findall("(?P<weight>[0-9]+) (?P<dst>[^ ]+ [^ ]+) bag(s)?", line)
  for m in dst_match:
    edges += [ (src, m[1], int(m[0])) ]

  return edges


inputs = []
with open("7.txt", "r") as f:
  inputs = [ l.strip() for l in f.readlines() ]


G = nx.DiGraph()

for i in inputs:
  edges = text_to_edges(i)
  G.add_weighted_edges_from(edges)


# Part A: How many colors can reach "shiny gold" ?
iG = G.reverse()
print("Part A: {}".format(len(nx.descendants(iG, "shiny gold"))))


# Part B: How many bags do you need to stuff one compliant "shiny gold"?
def bag_count(G, src):
  contents = 1
  for d in G.successors(src):
    weight = G.get_edge_data(src,d)["weight"]
    contents += weight * bag_count(G, d)
  return contents

n_bags = bag_count(G, "shiny gold") - 1

print("Part B: {}".format(n_bags))

