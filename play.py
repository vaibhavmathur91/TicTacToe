#!/usr/bin/env python3
from game import TicTac


class Main:
    def __init__(self):
        self.grid_len = 0
        self.moves_to_win = 0
        self.cur_row = 0
        self.cur_col = 0

    def execute_game(self):
        grid_check = True
        while grid_check:
            grid_count = input("\nEnter Grid length (Press q quit to exit !!) ")
            if grid_count.isdigit():
                self.grid_len = int(grid_count)
                grid_check = False
            elif grid_count == "q" or grid_count == "Q":
                break
            else:
                print("Please enter valid numbers !!")
        moves_check = True
        while moves_check:
            moves_count = input("\nEnter required moves to win (Press q quit to exit !!) ")
            if moves_count.isdigit():
                self.moves_to_win = int(moves_count)
                moves_check = False
            elif moves_count == "q" or moves_count == "Q":
                break
            else:
                print("Please enter valid numbers !!")
        tic_tac_game = TicTac(self.grid_len, self.moves_to_win)
        while True:
            if tic_tac_game.is_game_finished():
                print("\nPlayer" + str(tic_tac_game.winner) + " Won the Game !!")
                break
            print("\nPlayer" + str(tic_tac_game.get_cur_player()) + " Enter row and column of next placement!! ")
            cur_row_check = True
            while cur_row_check:
                cur_row = input(" Enter Row (0 to " + str(self.grid_len) + ") : ")
                if cur_row.isdigit():
                    self.cur_row = int(cur_row)
                    cur_row_check = False
                else:
                    print("Please enter valid numbers !!")
            cur_col_check = True
            while cur_col_check:
                cur_col = input(" Enter Column (0 to " + str(self.grid_len) + ") : ")
                if cur_col.isdigit():
                    self.cur_col = int(cur_col)
                    cur_col_check = False
                else:
                    print("Please enter valid numbers !!")
            if tic_tac_game.check_if_valid(self.cur_row, self.cur_col):
                tic_tac_game.make_move(self.cur_row, self.cur_col)
            else:
                print("Invalid Position !!")
