from Mancala import *
from random import seed


def minimax(board, player, depth, max_depth = 7):

    if check_terminal(board) or depth == max_depth:
        return utility(board)

    if player == 1:
        value = -np.inf
        for move in all_availables(board, 1):
            next_board, extra_move = move_stones(board, move, 1)

            if extra_move:
                value = max(value, minimax(next_board, 1, depth))
            else:
                value = max(value, minimax(next_board, 2,depth+1))

        return value

    if player == 2:
        value = np.inf
        for move in all_availables(board, 2):
            next_board, extra_move = move_stones(board, move, 2)

            if extra_move:
                value = min(value, minimax(next_board, 2, depth))
            else:
                value = min(value, minimax(next_board, 1, depth+1))

        return value


def minimax_alphabeta(board, player, depth,  alpha=-np.inf, beta=np.inf, max_depth=5):

    if check_terminal(board) or depth == max_depth:
        return utility(board)

    if player == 1:
        value = -np.inf
        for move in all_availables(board, 1):
            next_board, extra_move = move_stones(board, move, 1)

            if extra_move:
                value = max(value, minimax_alphabeta(next_board, 1, depth, alpha, beta))
            else:
                value = max(value, minimax_alphabeta(next_board, 2, depth + 1, alpha, beta))

            if value >= beta: break
            alpha = max(value, alpha)

        return value

    if player == 2:
        value = np.inf
        for move in all_availables(board, 2):
            next_board, extra_move = move_stones(board, move, 2)

            if extra_move:
                value = min(value, minimax_alphabeta(next_board, 2, depth, alpha, beta))
            else:
                value = min(value, minimax_alphabeta(next_board, 1, depth + 1, alpha, beta))

            if value <= alpha: break
            beta = min(value, beta)

        return value

def score_move(board, move):
    next_board, extra_move = move_stones(board, move, 1)

    if extra_move:
        return  minimax(next_board, 1, 1)
    else:
        return minimax(next_board, 2, 2)


def score_move_alphabeta(board, move):
    next_board, extra_move = move_stones(board, move, 1)

    if extra_move:
        return  minimax_alphabeta(next_board, 1, 1)
    else:
        return minimax_alphabeta(next_board, 2, 2)


def agent_minimax(board):
    child_nodes = np.array(all_availables(board, 1))
    evaluated_child_nodes = np.array([score_move(board, move) for move in child_nodes])
    bests = child_nodes[evaluated_child_nodes == max(evaluated_child_nodes)]

    return choice(bests.tolist())


def agent_minimax_alphabeta(board):
    child_nodes = np.array(all_availables(board, 1))
    evaluated_child_nodes = np.array([score_move_alphabeta(board, move) for move in child_nodes])
    bests = child_nodes[evaluated_child_nodes == max(evaluated_child_nodes)]

    return choice(bests.tolist())

def agent_random(board):
    child_nodes = np.array(all_availables(board, 2))
    return choice(child_nodes.tolist())




