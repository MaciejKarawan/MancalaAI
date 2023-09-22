from MinimaxMancala import agent_minimax_alphabeta
from MCTS import MCTS
from Mancala import *

def game():
    board = make_board()
    round = 1
    player = 1

    while check_terminal(board) is not True:

        if player == 1:
            move = agent_minimax_alphabeta(board)
            board, extra = move_stones(board, move, 1)

            if extra:
                player = 1
            else:
                player =2

        if player == 2:
            agent = MCTS(board, 5)
            move = agent.get_move()
            board, extra = move_stones(board, move, 2)

            if extra:
                player = 2
            else:
                player =1


    if board[6] > board[13]:
        print([1, board[6], board[13]])

    if board[6] < board[13]:
        print([2, board[6], board[13]])

    if board[6] == board[13]:
        print(['remis', board[6]])


game()