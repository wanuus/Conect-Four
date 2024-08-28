from board import Board
import time
import random
from gamealgorithms import make_move, is_terminal_game, winning_move, Move_Options



# GAME LINK
# http://kevinshannon.com/connect4/


def main():
    board = Board()
    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)

        # YOUR CODE GOES HERE
        column = make_move(game_board, 5, 1, "alpha")

        #print(column)
        board.select_column(column)

        time.sleep(3)

if __name__ == "__main__":
    main()
