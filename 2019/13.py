#!/usr/bin/env python3

from intcode import load_prog, run_prog
import time

class BricksMonitor:
  def __init__(self):
    self.termbuf = []
    self.score = 0
    self.frame = 0
    self.msg = ""

    self.tileset = {
                     0: " ",
                     1: "#",
                     2: "=",
                     3: "_",
                     4: "O"
                   }
    self.draw()

  def render(self, tile):
    if tile in self.tileset: return self.tileset[tile]
    return "^"  # Unknown tile

  def draw(self):
    sys.stdout.write("\033[2J")
    for l in self.termbuf:
      row = "".join([ self.render(tile) for tile in l ])
      print(row)
    self.hud()

  def hud(self):
    display = "Score: {}   {}".format(self.score, self.msg)
    sys.stdout.write("\033[{};{}H{}".format(len(self.termbuf)+1, 1, display))
    #sys.stdout.write("{}\n".format(display))


  def update(self, vm):
    if (len(vm.stdout) < 3): return

    x,y,tile = vm.stdout[:3]
    vm.stdout = vm.stdout[3:]

    if (x == -1 and y == 0):
      self.score = tile

    else:

      self.termbuf = grow(self.termbuf, y+1, [])
      self.termbuf[y] = grow(self.termbuf[y], x+1, 0)

      self.termbuf[y][x] = tile

      if tile == 4:
        self.frame += 1
        #time.sleep(0.1)

      sys.stdout.write("\033[{};{}H{}".format(y, x+1, self.render(tile)))

    self.hud()

class CheatStick:
  def __init__(self, monitor):
    self.monitor = monitor
    self.frame = 0

  def find_col(self, tile):
    for row in self.monitor.termbuf:
      if tile in row:
        return row.index(tile)
    return -1

  def update(self, vm):
    if len(vm.stdin) != 0: return
    if (self.monitor.frame == self.frame): return

    paddle = self.find_col(3)
    ball = self.find_col(4)


    if (paddle < ball): vm.stdin = [1]
    elif (paddle > ball): vm.stdin = [-1]
    else: vm.stdin = [0]

    self.frame = self.monitor.frame

    self.monitor.msg = "Paddle: {}  Ball: {}  Move: {}".format(paddle, ball, vm.stdin[0])

vm = load_prog("13.txt")
vm.outdev = BricksMonitor()
run_prog(vm)

all_tiles = [ tile for row in vm.outdev.termbuf for tile in row ]
block_count = len(list(filter(lambda t: t==2, all_tiles)))

print()
print("Part A: {}".format(block_count))

vm = load_prog("13.txt")
vm.mem[0] = 2
vm.outdev = BricksMonitor()
vm.indev = CheatStick(vm.outdev)
run_prog(vm)
