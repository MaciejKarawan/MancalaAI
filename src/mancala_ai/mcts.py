from mancala_ai.rules import *
from mancala_ai.node import Node
from timeit import default_timer as timer


class MCTS:
    def __init__(self, board, time):
        self.board = board
        self.time = time
        self.root = Node(self.board, 2, None)

    def traverse(self):
        current_node = self.root

        while current_node.full_expanded() and check_terminal(current_node.get_board()) is not True:
            childs = np.array([child for child in current_node.childs])
            ucts = np.array([child.get_uct() for child in childs])
            bests = childs[ucts == max(ucts)]
            current_node = choice(bests.tolist())

        return current_node


    def expand(self, node):
        unvisited = node.get_unvisited_moves()
        move = choice(unvisited)
        node.append_child(move)

        return  node.get_childs()[-1]

    def simulation(self, node):
        current_board = node.get_board()
        current_player = node.get_player()

        while check_terminal(current_board) is not True:
            moves  = all_availables(current_board, current_player)
            move = choice(moves)
            next_board, extra_move = move_stones(current_board, move, current_player)

            current_board = next_board
            if extra_move == False:
                current_player = {1,2}.difference({current_player}).pop()

        return  result(current_board)


    def backpropagate(self, node, result):

        while node is not None:

            if result == 1:
                if node.player == 2:
                    node.update_stats(result)
                else:
                    node.update_stats()
            elif result == 0:
                if node.player == 2:
                    node.update_stats()
                else:
                    node.update_stats(result)
            else:
                node.update_stats(result)

            node = node.parent


    def get_move(self):
        start = timer()

        while timer() - start < self.time:
            leaf = self.traverse()

            if check_terminal(leaf.get_board()) is not True:
                new_leaf = self.expand(leaf)
            else:
                new_leaf = leaf

            result = self.simulation(new_leaf)
            self.backpropagate(new_leaf, result)

        moves  = all_availables(self.root.get_board(), self.root.player)
        visits = [child.visits for child in self.root.get_childs()]
        best = visits.index(max(visits))

        return moves[best]



### TEST




