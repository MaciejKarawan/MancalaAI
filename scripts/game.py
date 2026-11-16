from mancala_ai.minimax import agent_minimax_alphabeta
from mancala_ai.mcts import MCTS
from mancala_ai.rules import *


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

        if player == 2:
            agentmcts = MCTS(board, 20)
            move = agentmcts.get_move()
            board, extra = move_stones(board, move, 2)
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


if __name__ == "__main__":
    game()
