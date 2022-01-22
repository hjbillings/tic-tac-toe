"""
Created on Sat Jan 22 11:57:22 2022

@author: hanabillings
"""

import pygame as pg

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // COLS

LIGHT = (189, 214, 252)
DARK = (66, 135, 245)
BLACK = (0, 0, 0)


class Board:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # initialize 3x3 empty board

    def draw_board(self, win):
        win.fill(LIGHT)

        # iterate through each space on the board:
        for row in range(ROWS):
            for col in range(row%2, ROWS, 2):
                # left, top, width, height
                pg.draw.rect(win, DARK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            for col in range(COLS):
                if self.board[row][col] == 1:
                    # top_left = (row*SQUARE_SIZE, col*SQUARE_SIZE)
                    # top_right = ()
                    # bottom_left = ()
                    # bottom_right = ()
                    pg.draw.line(win, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE),
                                 ((row + 1) * SQUARE_SIZE, (col + 1) * SQUARE_SIZE), width=4)
                    pg.draw.line(win, BLACK, (row * SQUARE_SIZE, (col + 1) * SQUARE_SIZE),
                                 ((row + 1) * SQUARE_SIZE, col * SQUARE_SIZE), width=4)

                elif self.board[row][col] == 2:
                    pg.draw.ellipse(win, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                                    width=4)

    # makes (x, y) coordinates of mouse click a tuple
    def turn(self, pos):
        # convert x and y into positions in board matrix using division
        x = int(pos[0] // (WIDTH / COLS))
        y = int(pos[1] // (HEIGHT / ROWS))

        # if position is taken, print warning message and return -1
        if self.board[x][y] != 0:
            print("Space already claimed — choose another.")
            return -1
        # if position is empty, set space on board and return 0
        else:
            self.board[x][y] = 1
            return 0

# enemy will return coordinate

