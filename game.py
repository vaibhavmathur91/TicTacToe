#!/usr/bin/env python3
class Position:
    def __init__(self):
        self.is_filled = False
        self.top = 0
        self.top_r = 0
        self.right = 0
        self.right_r = 0
        self.bottom = 0
        self.bottom_l = 0
        self.left = 0
        self.left_l = 0

    def is_not_filled(self):
        return not self.is_filled

    def mark_filled(self, val):
        self.is_filled = True
        self.top = val
        self.top_r = val
        self.right = val
        self.right_r = val
        self.bottom = val
        self.bottom_l = val
        self.left = val
        self.left_l = val


class Players:
    def __init__(self, id_number):
        self.id_number = id_number
        self.val = None
        self.has_completed = False

    def __repr__(self):
        return "player" + str(self.id_number)

    def get_id(self):
        return self.id_number

    def get_val(self):
        return self.val


class TicTac:
    def __init__(self, grid, moves_to_win):
        self.grid_len = grid
        self.moves_to_win = moves_to_win
        # self.board = [[Position() for _ in range(grid)] for _ in range(grid)]
        self.board = [[0 for _ in range(grid)] for _ in range(grid)]
        self.players = self._create_players()
        self.turn_index = 0
        self.is_finished = False
        self.winner = None

    @staticmethod
    def _create_players():
        player1 = Players(0)
        player1.val = -1
        player2 = Players(1)
        player2.val = 1
        return [player1, player2]

    def mark_game_finish(self, player_id):
        self.is_finished = True
        self.winner = player_id

    def is_game_finished(self):
        return self.is_finished

    def which_player_turn(self):
        return self.players[self.turn_index]

    def get_cur_player(self):
        return self.players[self.turn_index].get_id()

    def check_if_valid(self, row, col):
        # if self._check_if_valid_position(row, col) and self.board[row][col].is_not_filled():
        if self._check_if_valid_position(row, col) and self.board[row][col] == 0:
            return True
        return False

    def _check_if_valid_position(self, row, col):
        if (0 <= row < self.grid_len) and (0 <= col < self.grid_len):
            return True
        return False

    def change_players_turn(self):
        if self.is_game_finished():
            return
        self.turn_index = (self.turn_index + 1) % 2

    def _set_values(self, row, col, player_id):
        if self._check_if_valid_position(row-1, col):
            self.board[row][col].top += self.board[row-1][col].top
            if self.board[row][col].top == self.moves_to_win:
                self.mark_game_finish(player_id)
        if self._check_if_valid_position(row-1, col+1):
            self.board[row][col].top_r += self.board[row-1][col+1].top_r
            if self.board[row][col].top_r == self.moves_to_win:
                self.mark_game_finish(player_id)
        if self._check_if_valid_position(row, col+1):
            self.board[row][col].right += self.board[row][col+1].right
            if self.board[row][col].right == self.moves_to_win:
                self.mark_game_finish(player_id)
        if self._check_if_valid_position(row+1, col+1):
            self.board[row][col].right_r += self.board[row+1][col+1].right_r
            if self.board[row][col].right_r == self.moves_to_win:
                self.mark_game_finish(player_id)
        if self._check_if_valid_position(row+1, col):
            self.board[row][col].bottom += self.board[row+1][col].bottom
            if self.board[row][col].bottom == self.moves_to_win:
                self.mark_game_finish(player_id)
        if self._check_if_valid_position(row + 1, col-1):
            self.board[row][col].bottom_l += self.board[row + 1][col-1].bottom_l
            if self.board[row][col].bottom_l == self.moves_to_win:
                self.mark_game_finish(player_id)
        if self._check_if_valid_position(row, col-1):
            self.board[row][col].left += self.board[row][col-1].left
            if self.board[row][col].left == self.moves_to_win:
                self.mark_game_finish(player_id)
        if self._check_if_valid_position(row-1, col-1):
            self.board[row][col].left_l += self.board[row-1][col-1].left_l
            if self.board[row][col].left_l == self.moves_to_win:
                self.mark_game_finish(player_id)

    def _check_horizontal(self, row, col, val):
        count = 0
        for i in range(max(0, col-self.moves_to_win), min(col+self.moves_to_win, self.grid_len)):
            if self.board[row][i] == val:
                count += 1
                if count == self.moves_to_win:
                    return True
            else:
                count = 0
        return False

    def _check_vertical(self, row, col, val):
        count = 0
        for i in range(max(0, row-self.moves_to_win), min(row+self.moves_to_win, self.grid_len)):
            if self.board[i][col] == val:
                count += 1
                if count == self.moves_to_win:
                    return True
            else:
                count = 0
        return False

    def _check_diagonal_from_top_left(self, row, col, val):
        count = 0
        for i in range(max(0, col-self.moves_to_win), min(col+self.moves_to_win, self.grid_len)):
            if self._check_if_valid_position(row+i-col, i):
                if self.board[row+i-col][i] == val:
                    count += 1
                    if count == self.moves_to_win:
                        return True
                else:
                    count = 0
        return False

    def _check_diagonal_from_bottom_left(self, row, col, val):
        count = 0
        for i in range(max(0, col-self.moves_to_win), min(col+self.moves_to_win, self.grid_len)):
            if self._check_if_valid_position(row+col-i, i):
                if self.board[row+col-i][i] == val:
                    count += 1
                    if count == self.moves_to_win:
                        return True
                else:
                    count = 0
        return False

    def _check_winner(self, row, col, player):
        val = player.get_val()
        if self._check_horizontal(row, col, val) or self._check_vertical(row, col, val) or self._check_diagonal_from_top_left(row, col, val) or self._check_diagonal_from_bottom_left(row, col, val):
            self.mark_game_finish(val)

    def _mark_next_position(self, row, col, player):
        # self.board[row][col].mark_filled(player.get_val())
        self.board[row][col] = player.get_val()
        # self._set_values(row, col, player.get_val())
        self._check_winner(row, col, player)

    def make_move(self, row, col):
        cur_player = self.which_player_turn()
        self._mark_next_position(row, col, cur_player)
        self.change_players_turn()
