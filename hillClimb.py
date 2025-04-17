#!/usr/bin/env python3

# Hill climbing by min conflicts to solve many queens problem
# Used primitive random reset for local minimum detection

import random
from argparse import ArgumentParser

DEBUG = False
SHOW_STEPS = False
N_QUEENS = None

class Board():

  def __init__(self):
    self.queens = [ random.randint(0, N_QUEENS - 1) for x in range(N_QUEENS) ]

  def n_constraints_broken(self, row, col):
    constraints_broken = 0

    for curr_row, curr_col in enumerate(self.queens):
      if row == curr_row: continue

      # same column
      if col == curr_col:
        constraints_broken += 1

      # same diagonal positive
      if curr_row == curr_col - col + row:
        constraints_broken += 1
      
      # same diagonal negative
      if curr_row == -curr_col + col + row:
        constraints_broken += 1

    return constraints_broken
  
  def print_board(self):
    for row, queen_col in enumerate(self.queens):
      for col in range(N_QUEENS):
        if queen_col == col:
          print('👑', end='')
        elif (row + col) % 2 == 0:
          print('⬜', end='')
        else:
          print('⬛', end='')
      print()
    print()

  def solve(self):
    prev_state = None
    while True:
      constraints_broken = [(self.n_constraints_broken(row, col), row) for row, col in enumerate(self.queens)]
      val, row = max(constraints_broken, key=lambda c: c[0])

      if val == 0:
        break

      self.queens[row] = min([n for n in range(N_QUEENS)], key=lambda n: self.n_constraints_broken(row, n))
      curr_state = [self.n_constraints_broken(row, col) for row, col in enumerate(self.queens)]

      if prev_state == curr_state:
        if DEBUG or SHOW_STEPS: print("Local minimum detected - Random Reset")
        self.reset()
      
      prev_state = curr_state

      if SHOW_STEPS: self.print_board()
    
    if DEBUG: print([self.n_constraints_broken(row, col) for row, col in enumerate(self.queens)])

  def reset(self):
    self.queens = [ random.randint(0, N_QUEENS - 1) for x in range(N_QUEENS) ]

parser = ArgumentParser()
parser.add_argument('-d', '--debug', action="store_true")
parser.add_argument('nqueens', default=8)
parser.add_argument('-s', '--steps', action="store_true")
args = parser.parse_args()

DEBUG = args.debug
SHOW_STEPS = args.steps
N_QUEENS = int(args.nqueens)

board = Board()
print(board.queens)
print("Initial Random Board")
board.print_board()
board.solve()
print('Solved Board')
board.print_board()
