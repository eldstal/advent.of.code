#!/usr/bin/env python3

import aoc
import re

_,lines = aoc.get_input(7)

OP = {
   "ASSIGN": lambda a,b: a,
   "NOT":    lambda a,b: a ^ 0xFFFF,
   "AND":    lambda a,b: a & b,
   "OR":     lambda a,b: a | b,
   "RSHIFT": lambda a,b: a >> b,
   "LSHIFT": lambda a,b: a << b,
}

E_EXPR   = re.compile(r"^(?P<expr>.*) -> (?P<dest>\w*)$")
E_CONST  = re.compile(r"^(?P<val>[0-9]+)$")
E_ASSIGN = re.compile(r"^(?P<a>\w+)$")
E_UNARY  = re.compile(r"^(?P<op>[A-Z]+) (?P<a>\w*)$")
E_BINARY = re.compile(r"^(?P<a>\w+) (?P<op>[A-Z]+) (?P<b>\w+)$")

# output -> (operand, operand, operation)
nodes = {}

def get_value(wire):
  if wire is None: return 0
  if type(wire) == int: return wire

  assert(wire in nodes)

  expr = nodes[wire]

  if type(expr) == int:
    return expr

  a, b, op, fun = expr
  #print(wire, a, op, b)

  a = get_value(a)
  b = get_value(b)
  v = fun(a, b) & 0xFFFF

  # Memorize
  nodes[wire] = v

  return v

def parse_operand(a):
  c = E_CONST.match(a)
  if c is None: return a

  return int(a)

def parse_expr(line):
  e = E_EXPR.match(line)
  if e is None:
    raise RuntimeError(line)

  dest = e.group("dest")

  a = E_ASSIGN.match(e.group("expr"))
  if a is not None:
    return dest, (parse_operand(a.group("a")), None, "ASSIGN", OP["ASSIGN"])

  u = E_UNARY.match(e.group("expr"))
  if u is not None:
    return dest, (parse_operand(u.group("a")), None, u.group("op"), OP[u.group("op")])

  b = E_BINARY.match(e.group("expr"))
  if b is not None:
    return dest, (parse_operand(b.group("a")), parse_operand(b.group("b")), b.group("op"), OP[b.group("op")])

  raise RuntimeError(line)

for l in lines:
  dest, operation = parse_expr(l)
  nodes[dest] = operation

a = get_value("a")
print(f"Part 1: a = {a}")


nodes = {}
for l in lines:
  dest, operation = parse_expr(l)
  nodes[dest] = operation

nodes["b"] = a

new_a = get_value("a")
print(f"Part 2: a = {new_a}")
