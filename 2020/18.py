#!/usr/bin/env python3

tokens = ( 'NUM', 'MULT', 'ADD', 'LPAR', 'RPAR' )

def Lexer():
  import ply.lex as lex

  t_ADD  = r'\+'
  t_MULT = r'\*'
  t_LPAR = r'\('
  t_RPAR = r'\)'

  def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

  t_ignore = ' \t'

  def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

  return lex.lex()

def ParserA():
  import ply.yacc as yacc


  def p_expression_add(p):
    'expression : expression ADD top_prio'
    p[0] = p[1] + p[3]

  def p_expression_mult(p):
    'expression : expression MULT top_prio'
    p[0] = int(p[1] * p[3])

  def p_expression_top(p):
    'expression : top_prio'
    p[0] = int(p[1])

  def p_term_parens(p):
    'top_prio : LPAR expression RPAR'
    p[0] = p[2]

  def p_term_num(p):
    'top_prio : NUM'
    p[0] = int(p[1])

  def p_error(p):
    print("Syntax error in input!")

  return yacc.yacc()

def ParserB():
  import ply.yacc as yacc

  def p_expression_mult(p):
    'expression : expression MULT mid_prio'
    p[0] = int(p[1] * p[3])

  def p_expression_mid(p):
    'expression : mid_prio'
    p[0] = int(p[1])

  def p_mid_sum(p):
    'mid_prio : mid_prio ADD top_prio'
    p[0] = p[1] + p[3]

  def p_mid_top(p):
    'mid_prio : top_prio'
    p[0] = p[1]

  def p_term_parens(p):
    'top_prio : LPAR expression RPAR'
    p[0] = p[2]

  def p_term_num(p):
    'top_prio : NUM'
    p[0] = int(p[1])

  def p_error(p):
    print("Syntax error in input!")

  return yacc.yacc()


def compute(code, precedence=False):
  lexer = Lexer()
  lexer.input(code)

  if not precedence:
    parser = ParserA()
  else:
    parser = ParserB()
  return parser.parse(code, lexer)

  #for tok in lexer:
  #  print(tok)
  #return 71




def partA():
  assert(compute("1 + 2 * 3 + 4 * 5 + 6") == 71)
  assert(compute("1 + (2 * 3) + (4 * (5 + 6))") == 51)
  assert(compute("2 * 3 + (4 * 5)") == 26)
  assert(compute("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437)
  assert(compute("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240)
  assert(compute("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632)

  total = 0
  inputs = []
  with open("18.txt", "r") as f:
    for code in f.readlines():
      total += compute(code.strip())

  print("Part A: {}".format(total))


def partB():
  assert(compute("1 + 2 * 3 + 4 * 5 + 6", True) == 231)
  assert(compute("1 + (2 * 3) + (4 * (5 + 6))", True) == 51)
  assert(compute("2 * 3 + (4 * 5)", True) == 46)
  assert(compute("5 + (8 * 3 + 9 + 3 * 4 * 3)", True) == 1445)
  assert(compute("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", True) == 669060)
  assert(compute("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", True) == 23340)

  total = 0
  inputs = []
  with open("18.txt", "r") as f:
    for code in f.readlines():
      total += compute(code.strip(), True)

  print("Part B: {}".format(total))

partB()
