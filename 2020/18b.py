#!/usr/bin/env python3
import re

def eat_parens(code):
  assert(code[0] == "(")
  depth = 1
  for p in range(1, len(code)):
    if code[p] == "(": depth += 1
    if code[p] == ")": depth -= 1
    if depth == 0: break
  if depth != 0: raise RuntimeError(code)

  return code[1:p], code[p+1:]

def eat_num(code):
  m = re.match("^[0-9]+", code)
  if m is None: raise RuntimeError(code)

  num = m.group(0)

  return int(num), code[len(num):]

def eat_term(code):
  if code[0] == "(":
    return eat_parens(code)
  else:
    return eat_num(code)

def eat_op(code):
  if code[0] in "*+":
    return code[0], code[1:]
  raise RuntimeError(code)

def compute_A(code):
  code = code.replace(" ", "")


  operand,code = eat_term(code)
  if type(operand) == int: lhs = operand
  else: lhs = compute_A(operand)

  stack = lhs

  while code != "":

    operator,remainder = eat_op(code)
    operand,remainder = eat_term(remainder)

    if type(operand) == int: rhs = operand
    else: rhs = compute_A(operand)

    if operator == "+": stack += int(rhs)
    elif operator == "*": stack *= int(rhs)
    else: raise RuntimeError(code)

    code = remainder

  return stack


assert(compute_A("1 + 2 * 3 + 4 * 5 + 6") == 71)
assert(compute_A("1 + (2 * 3) + (4 * (5 + 6))") == 51)
assert(compute_A("2 * 3 + (4 * 5)") == 26)
assert(compute_A("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437)
assert(compute_A("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240)
assert(compute_A("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632)

total = 0
with open("18.txt", "r") as f:
  for code in f.readlines():
    total += compute_A(code.strip())

print("Part A: {}".format(total))




def compute_B(code):
  return 0

assert(compute_B("1 + 2 * 3 + 4 * 5 + 6") == 231)
assert(compute_B("1 + (2 * 3) + (4 * (5 + 6))") == 51)
assert(compute_B("2 * 3 + (4 * 5)") == 46)
assert(compute_B("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445)
assert(compute_B("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060)
assert(compute_B("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340)


total = 0
with open("18.txt", "r") as f:
  for code in f.readlines():
    total += compute_B(code.strip())

print("Part B: {}".format(total))


