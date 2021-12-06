#!/usr/bin/env python3
import numpy as np
import math

def mat_to_int(m):
  l = m.tolist()
  ret = 0
  for b in range(len(l)):
    ret |= l[b] << b
  return ret

def reverse_int(v, width=10):
  ret = 0
  for i in range(width):
    ret = (ret << 1) | ((v >> i) & 0x1)
  return ret

class Tile:
  # Parse a text blob
  # tile gets integer edges n,e,s,w
  # tile gets list edges = [n,e,s,w,n',e',s',w'] for convenience
  # tile als  gets integer id
  # tile contains a px matrix
  def __init__(self, text):
    lines = [ l.strip() for l in text.strip().split("\n") ]
    self.id = int(lines[0].split(" ")[1][:-1])

    pixels = [ [ c == "#" for c in line ] for line in lines[1:] ]

    self.px = np.array(pixels)
    self.encode_edges()

  def __str__(self):
    return "Tile {} : <{}, {}, {}, {}>".format(self.id, self.n, self.e, self.s, self.w)

  def __repr__(self):
    return self.__str__()

  def encode_edges(self):
    self.n = mat_to_int(self.px[0,:])
    self.s = mat_to_int(self.px[-1,:])
    self.w = mat_to_int(self.px[:,0])
    self.e = mat_to_int(self.px[:,-1])

    self.edges =  [ self.n, self.e, self.s, self.w ]
    self.edges += [ reverse_int(n) for n in self.edges ]


  # Rotate some number of times, counter-clockwise
  def rotate(self, n=1):
    self.px = np.rot90(self.px, n, (0,1))
    self.encode_edges()

  def fliplr(self):
    self.px = np.fliplr(self.px)
    self.encode_edges()

  def flipud(self):
    self.px = np.flipud(self.px)
    self.encode_edges()



tiles = {}
with open("20_test.txt","r") as f:
  text_blocks = f.read().split("\n\n")
  for b in text_blocks:
    t = Tile(b)
    tiles[t.id] = t

W = int(math.sqrt(len(tiles)))
H = len(tiles) // W
E = 2*W + 2*H - 4
assert(W * H == len(tiles))
print("{} tiles loaded.".format(len(tiles)))
print("{}x{} arrangement".format(H, W))
print("{} edge tiles".format(E))


# Start with some basic analysis.
# Hypothesis: All edge pieces have unique combos
# Since the image can be flipped and rotated and whatnot,
# we have to assume any edge can also be reversed
edges = {}
for t in tiles.values():
  for e in t.edges:
    if e in edges:
      edges[e].add(t.id)
    else:
      edges[e] = set([t.id])

uniques = [ e for e in edges if len(edges[e]) == 1 ]
print("{} unique edge values".format(len(uniques)))
