#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#fig, ax = plt.subplots()
xdata, ydata, zdata = [], [], []
ln, = ax.plot([2], [2], "ro", zdir='z')


def init():
  ax.set_xlim(0, 2*np.pi)
  ax.set_ylim(-1, 1)
  ax.set_zlim(-1, 1)
  return ln,

def update(frame):
  xdata.append(frame)
  ydata.append(np.sin(frame))
  #zdata.append(frame)
  ln.set_data(xdata, ydata)
  return ln,


def vis_run(A, ticks):
  ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), init_func=init, blit=True)
  plt.show()

  #for 

if __name__ == "__main__":
  vis_run(None, 6)



