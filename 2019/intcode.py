import time
import sys
from pynput import keyboard

class VM:
  def __init__(self):
    self.mem = []

    # I/O
    self.stdin = []
    self.stdout = []

    # Peripherals
    self.indev = None
    self.outdev = None

    # Registers
    self.ip = 0
    self.base = 0

def grow(lst, size, padding):
  return lst + [padding]*(size - len(lst) + 1)

def peek(vm, addr):
  vm.mem = grow(vm.mem, addr, 0)
  return vm.mem[addr]

def poke(vm, pos, mode, val):
  _,addr = resolve(vm, mode, pos)
  vm.mem[addr] = val


def resolve(vm, mode, arg):
  # Position mode
  if (mode == 0): return peek(vm, arg), arg

  # Immediate mode
  elif (mode == 1): return arg, 0

  # Relative mode
  elif (mode == 2): return peek(vm,arg+vm.base), arg+vm.base


def op1(vm, modes, args, vals):
  poke(vm, args[2], modes[2], vals[0] + vals[1])

def op2(vm, modes, args, vals):
  poke(vm, args[2], modes[2], vals[0] * vals[1])

def op3(vm, modes, args, vals):
  poke(vm, args[0], modes[0], vm.stdin[0])
  vm.stdin = vm.stdin[1:]

def op4(vm, modes, args, vals):
  vm.stdout += [ vals[0] ]

def op5(vm, modes, args, vals):
  if vals[0] != 0:
    vm.ip,_ = resolve(vm, modes[1], args[1])

def op6(vm, modes, args, vals):
  if vals[0] == 0:
    vm.ip,_ = resolve(vm, modes[1], args[1])

def op7(vm, modes, args, vals):
  if vals[0] < vals[1]:
    poke(vm, args[2], modes[2], 1)
  else:
    poke(vm, args[2], modes[2], 0)

def op8(vm, modes, args, vals):
  if vals[0] == vals[1]:
    poke(vm, args[2], modes[2], 1)
  else:
    poke(vm, args[2], modes[2], 0)

def op9(vm, modes, args, vals):
  vm.base += vals[0]

def op99(vm, modes, args, vals):
  pass

# opcode: arg_length, fun
OPS = {
  1: (3, op1),    # add
  2: (3, op2),    # mul

  3: (1, op3),    # read
  4: (1, op4),    # write

  5: (2, op5),    # jump-if-true
  6: (2, op6),    # jump-if-false

  7: (3, op7),    # less-than
  8: (3, op8),    # equal

  9: (1, op9),    # mbase

  99: (0, op99)
}




def load_prog(path):
  vm = VM()
  with open(path, "r") as f:
    vm.mem = [ int(v) for v in f.read().split(",") ]
  return vm


def fetch(vm, ip):

  opcode = vm.mem[ip] % 100
  modes = [
            int(vm.mem[ip] / 100) % 10,
            int(vm.mem[ip] / 1000) % 10,
            int(vm.mem[ip] / 10000) % 10,
          ]

  # If this fails, it's an invalid opcode
  try:
    n_args,_ = OPS[opcode]
  except Exception as e:
    print("Invalid opcode {} at ip={}".format(opcode, ip))
    raise e

  args = vm.mem[ip+1 : ip+1+n_args]
  modes = modes[:n_args]

  return opcode, modes, args, ip+1+n_args

def prefetch(vm, modes, args):
  return [ resolve(vm, modes[i], args[i])[0] for i in range(len(args)) ]

def execute(vm, opcode, modes, args):
  if opcode == 99:
    return True

  _,fn = OPS[opcode]

  vals = prefetch(vm, modes, args)

  #print(opcode, args, vals)
  fn(vm, modes, args, vals)
  return False


def run_prog(vm):
  terminate = False

  while not terminate:
    ip = vm.ip
    opcode,mode,args,vm.ip = fetch(vm, vm.ip)
    terminate = execute(vm, opcode, mode, args)

    if (vm.outdev is not None):
      vm.outdev.update(vm)

    if (vm.indev is not None):
      vm.indev.update(vm)

