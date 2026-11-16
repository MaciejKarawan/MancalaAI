import numpy as np
from random import choice

# Początkowa plansza
## Pozycje 1 gracza: 0-5
## Pozycje 2 gracza: 7-12
## Mankale: 6 i 13

def make_board():
    board = np.ones(14, dtype=int)*4
    board[6] = 0
    board[13] = 0
    return board


def move_stones(board, x, player):
    new_board = board.copy()
    n = new_board[x]
    new_board[x] = 0
    extra_move = False

    if player == 1:
        work_board = new_board[:13]

        for i in range(x+1, n+x+1):
            i = i % 13
            work_board[i] += 1

        # check if extra move or stealing occur

        last_hole = (n+x)%13

        if last_hole == 6:
            extra_move = True

        if last_hole < 6:
            if work_board[last_hole] == 1:

                work_board[6] += work_board[last_hole] + work_board[-(last_hole + 1)]
                work_board[last_hole] = 0
                work_board[-(last_hole + 1)] = 0


    if player == 2:
        work_board = np.delete(new_board, 6)

        for i in range(x, n + x):
            i = i % 13
            work_board[i] += 1

        # check if extra move or stealing occur

        last_hole = (n+x - 1)%13

        if last_hole == 12:
            extra_move = True

        if last_hole > 5 and last_hole < 12:
            if work_board[last_hole] == 1:

                work_board[12] += work_board[last_hole] + work_board[-(last_hole + 2)]
                work_board[last_hole] = 0
                work_board[-(last_hole + 2)] = 0

        new_board = np.insert(work_board, 6, new_board[6])

    return new_board, extra_move


def all_availables(board, player):
    if player == 1:
        return [i for i in range(6) if board[i] > 0]
    if player == 2:
        return [i for i in range(7,14) if board[i] > 0]



def check_terminal(board):
    terminal = np.zeros(6, dtype=int)

    if np.array_equal(board[:6], terminal):
        return True
    if np.array_equal(board[7:13], terminal):
        return True

    return False


def utility(board):
    return board[6] - board[13]

def result(board):
    result = -utility(board)

    if result > 0:
        return 1
    elif result < 0:
        return 0

    return 0.5