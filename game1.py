from MinimaxMancala import agent_minimax_alphabeta
from MCTS1 import MCTS1
from Mancala import *


def game():
    board = make_board()
    round = 0
    player = 1
    history = [board]

    while check_terminal(board) is not True:

        if player == 1:
            move = agent_minimax_alphabeta(board)
            board, extra = move_stones(board, move, 1)
            history.append(board)

            if extra:
                player = 1
            else:
                player = 2
                if round > 3: agentmcts.update_root(board)

        if player == 2:

            if round < 4:
                agentmcts = MCTS1(board, 60)
            else:
                pass

            move = agentmcts.get_move()
            board, extra = move_stones(board, move, 2)
            agentmcts.update_root(board)

            history.append(board)

            if extra:
                player = 2
            else:
                player = 1

        round += 1


    print(board)
    print(round)

    for i in history:
        print(i)


game()