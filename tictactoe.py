"""
Created on Sat Jan 22 11:56:46 2022

@author: hanabillings
"""

import pygame as pg
from tictactoe_utils import *
from board import WIDTH, HEIGHT, Board

WIN = pg.display.set_mode((WIDTH, HEIGHT))  # setting dimensions of screen display
pg.display.set_caption('Tic Tac Toe')  # display name of game
MESSAGES = ["tie!", "you won :)", "you lost :("]


def take_turn(player, tictactoe):
    if player == 1:
        # human player goes -- until valid
        valid = tictactoe.turn(pg.mouse.get_pos())
        # return -1 if the position chosen was invalid
        while valid == -1:
            valid = tictactoe.turn(pg.mouse.get_pos())
    else:
        pos = random_player(tictactoe.board)
        tictactoe.board[pos[0]][pos[1]] = 2
    # update + display board
    tictactoe.draw_board(WIN)
    pg.display.update()

    status = state(tictactoe.board)

    if status != -1:
        print("game over:", MESSAGES[status])
    # returns false if game is over, true otherwise
    return (status == -1)


def main():
    running = True
    timer = pg.time.Clock()
    tictactoe = Board()

    tictactoe.draw_board(WIN)
    pg.display.update()

    print("welcome to tic tac toe!") # prints in terminal

    while running:
        timer.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                # call take_turn with player
                running = take_turn(1, tictactoe)

                if not running:
                    break
                # call take_turn with "bot"
                pg.time.delay(1000)
                running = take_turn(2, tictactoe)

    pg.quit()  # quit game


if __name__ == "__main__":
    main()
