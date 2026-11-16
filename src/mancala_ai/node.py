from mancala_ai.rules import *
from math import log, sqrt


class Node:
    def __init__(self, board, player, parent):
        self.board = board
        self.player = player  # gracz który ma ruch w tym wierzchołku
        self.parent = parent
        self.unvisited_moves = all_availables(board, player)
        self.childs = []
        self.visits = 0
        self.wins = 0
        #self.total_plays = total_plays

    def get_board(self):
        return self.board
    def get_childs(self):
        return self.childs

    def get_player(self):
        return self.player

    def get_unvisited_moves(self):
        return self.unvisited_moves

    def update_unvisited_moves(self, move):
        self.unvisited_moves.remove(move)

    def append_child(self, move):
        next_board, extra_move = move_stones(self.board, move, self.player)
        if extra_move:
            child_node = Node(next_board, self.player, self)
        else:
            player = {1,2}.difference({self.player}).pop()
            child_node = Node(next_board, player, self)

        self.childs.append(child_node)
        self.update_unvisited_moves(move)

    def get_uct(self):
        c = sqrt(2)
        uct = self.wins/self.visits + c * sqrt(log(self.parent.visits)/self.visits)
        return uct

    def full_expanded(self):
        if self.get_unvisited_moves() == []:
            return True

        return False

    def update_stats(self, result=0):
        self.visits += 1
        self.wins += result

    def board_child(self, board):
        for child in self.get_childs():
            if np.array_equal(child.get_board(), board):
                return child

        return None






