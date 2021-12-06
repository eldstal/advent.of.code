#!/usr/bin/env python3
import math
import numpy as np

arrival = 0
buses = []
inputs = []
with open("13.txt", "r") as f:
  lines = f.readlines()
  arrival = int(lines[0].strip())
  buses = [ int(bid) for bid in lines[1].strip().split(",") if bid != "x"]


def departures_after(arrival, buses):
	# bus ID is also its departure frequency
	departs = [ math.ceil(arrival / freq)*freq for freq in buses ]
	return departs

departs = departures_after(arrival, buses)

# Find the earliest
idx = departs.index(min(departs))
best_bus = buses[idx]
best_depart = departs[idx]
wait_time = best_depart - arrival

print(arrival)
print(buses)
print("Part A: bus {} at {}: {}".format(best_bus, best_depart, best_bus * wait_time))



buses = []
positions = []
with open("13.txt", "r") as f:
  lines = f.readlines()
  arrival = int(lines[0].strip())
  pos = 0
  for bid in lines[1].strip().split(","):
    if bid != "x":
      buses += [ int(bid) ]
      positions += [pos]
    pos += 1


# https://rosettacode.org/wiki/Chinese_remainder_theorem

# (¤ is the congruence operator)
# t ¤ k-0 (mod buses[0])
# t ¤ k-1 (mod buses[1])
# t ¤ k-2 (mod buses[2])

def euclid(a, b):
	if a == 0 :
		return b,0,1

	gcd,x1,y1 = euclid(b%a, a)

	x = y1 - (b//a) * x1
	y = x1

	return gcd,x,y


def invmod(a, m):
	g, x, y = euclid(a, m)
	if g != 1:
		raise ValueError('modular inverse {},{} does not exist (gcd={})'.format(a, m, g))
	else:
		return x % m

def crt_gauss(n, N, a):
	ret = 0
	for i in range(len(n)):
		b = N // n[i]
		ret += a[i] * b * invmod(b, n[i])
	return ret

# Notation:
# x ¤ a_i (mod n_i)

#buses = [17, 13, 19] #3417
#positions = [0, 2, 3]

#buses = [ 67,7,59,61 ] #754018
#positions = [ 0, 1, 2, 3]

# CRT can find the time t+d of the last departure!
# The remainder, then, is k-pos so that
# the remainder on bus k is 0 and the remainder on bus 0 is k
k = max(positions)
remainders = [ k - pos for pos in positions ]

# 
n = buses
a = remainders
N = int(np.prod(n))

x = crt_gauss(n, N, a) % N

t = x - k

print("Part B: t={}".format(t))
