class VM:

  def __init__(self):
    self.reset()

  def reset(self):
    # Registers
    self.acc = 0
    self.ip = 0

    # List of [op, arg]
    self.prog = []

    # set of instructions executed
    self.trace = set()

  def load(self, path):
    with open(path, "r") as f:
      inputs = [ l.strip() for l in f.readlines() ]
      for l in inputs:
        op = l.split(" ")[0]
        arg = int(l.split(" ")[1])
        self.prog += [ [op, arg] ]

  def execute(self, op, arg):
    if op == "nop": return
    if op == "acc": self.acc += arg
    if op == "jmp": self.ip += arg - 1

  def status(self):
    if (self.ip in self.trace): return 2
    if (self.ip == len(self.prog)): return 0
    if (self.ip > len(self.prog)): return -1
    if (self.ip < 0): return -1
    return 1

  # Returns:
  # -1 if execution terminates abnormally
  # 0 if execution terminates normally
  # 1 if execution can continue
  # 2 if execution is about to repeat
  def step(self):

    if (self.ip in self.trace): return 2
    self.trace.add(self.ip)

    # fetch
    op, arg = tuple(self.prog[self.ip])
    self.ip += 1

    self.execute(op, arg)

    return self.status()
