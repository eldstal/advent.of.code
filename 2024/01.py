#!/usr/bin/env python3
import aoc
import frames
import asyncio

DAY=1

_, lines = aoc.get_input(DAY)
_, lines = aoc.get_test_input(DAY)

answer_a = 0

class App01(frames.AdventApp):

  async def on_ready(self, size):
    self.run_worker(self.load_input(), exclusive=True)

  async def load_input(self):

    for l in range(len(lines)):
      self.progress("input", "Input", l, len(lines))
      await asyncio.sleep(0.3)

    self.progress("parse", "Parse", 5, 20)


window = App01()
window.run()


print(f"Part 1: {answer_a}")
#print(aoc.post_result(day=DAY, part=1, value=answer_a, year=2022))


answer_b = 0

print(f"Part 2: {answer_b}")
#print(aoc.post_result(day=DAY, part=2, value=answer_b, year=2022))
