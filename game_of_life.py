import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import argparse
import time

# matplotlib.use('Qt5Agg')

class Board(object):
   def __init__(self, *size, seed='Random'):
      if seed == 'Random':
         self.state = np.random.randint(2, size=size)
      self.engine = Engine(self)
      self.iteration = 0

   def animate(self):
      i = self.iteration
      im = None
      plt.title("Conway's Game of Life")
      while True:
         if i == 0:
            plt.ion()
            im = plt.imshow(self.state, vmin=0, vmax=2, cmap=plt.cm.gray)
         else:
            im.set_data(self.state)
         i += 1
         self.engine.applyRules()
         print('Life Cycle: {} Birth: {} Survive: {}'.format(i, self.engine.nBirth, self.engine.nSurvive))
         plt.pause(0.01)
         yield self

class Engine(object):
   def __init__(self, board):
      self.state = board.state

   def countNeighbors(self):
      
      n = (self.state[0:-2,0:-2] + self.state[0:-2,1:-1] + self.state[0:-2,2:] +
          self.state[1:-1,0:-2] + self.state[1:-1,2:] + self.state[2:,0:-2] +
          self.state[2:,1:-1] + self.state[2:,2:])
      return n
   
   def applyRules(self):
      n = self.countNeighbors()
      state = self.state
      birth = (n == 3) & (state[1:-1,1:-1] == 0)
      survive = ((n == 2) | (n == 3)) & (state[1:-1,1:-1] == 1)
      state[...] = 0
      state[1:-1,1:-1][birth | survive] = 1 
      self.nBirth = np.sum(birth)
      self.nSurvive = np.sum(survive)
      return state

if __name__ == "__main__":
   ap = argparse.ArgumentParser(add_help = False) # Intilialize Argument Parser
   ap.add_argument('-h', '--height', default=500)
   ap.add_argument('-w', '--width', default=500)
   args = vars(ap.parse_args()) # Gather Arguments
   height = int(args['height'])
   width = int(args['width'])
   board = Board(width,height)
   for _ in board.animate(): ...
