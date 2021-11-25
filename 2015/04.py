#!/usr/bin/env python3

import multiprocessing as mp
import hashlib

salt = "ckczppom"

def smash5(seed, needle, a, b, q):
  for n in range(a,b):
    m = hashlib.md5()
    m.update((seed + str(n)).encode())
    d = m.hexdigest()
    if d[:len(needle)] == needle:
      q.put(n)
      break

def find_for_prefix(prefix="00000"):
  bottom = 1
  top = 10000000
  n_threads = 16

  q = mp.Queue()

  count_per_thread = (top-bottom) // n_threads

  args = [ ]
  for t in range(n_threads):
    a = t*count_per_thread
    b = a + count_per_thread
    args += [ (salt, prefix, a, b, q) ]

  threads = [ mp.Process(target=smash5, args=a) for a in args ]

  for t in threads:
    t.start()

  for t in threads:
    t.join()


  v = []
  while not q.empty():
    v.append(q.get())

  return min(v)

five = find_for_prefix("00000")
print(f"Part 1: {five}")


six = find_for_prefix("000000")
print(f"Part 1: {six}")

