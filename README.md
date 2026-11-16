# Mancala AI: Minimax vs. Monte Carlo Tree Search

**Game engine for Kalah-style Mancala with two AI agents, a depth-limited minimax with alpha-beta pruning and a UCT Monte Carlo Tree Search, played against each other.**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy)
![Topic](https://img.shields.io/badge/topic-game%20AI%20%7C%20search-blueviolet)

## Game

- 14-position board stored as a NumPy array: 6 pits per player plus two stores, with 4 stones per pit (48 in total)
- Sowing counter-clockwise, skipping the opponent's store
- **Extra move** when the last stone lands in your own store
- **Capture** when the last stone lands in an empty pit on your side: you take it and the stones opposite

## Agents

| Agent | Idea |
|---|---|
| **Minimax** | Exhaustive search to a fixed depth, with the store difference as the utility. Extra moves keep the same player at the same depth |
| **Minimax + alpha-beta** | The same search with alpha-beta pruning (default depth 5), so it can look deeper for the same cost |
| **MCTS (UCT)** | Selection with UCB1 (c = √2), expansion, random playouts and backpropagation within a per-move time budget. The most-visited child is played |
| **MCTS variant** | Keeps and re-roots the search tree between moves instead of rebuilding it each turn |
| Random | Baseline |

## Repository structure

```
src/mancala_ai/   rules.py (board, sowing, captures, terminal state, utility),
                  minimax.py, mcts.py, mcts_variant.py, node.py (UCT tree node)
scripts/          game (alpha-beta vs. MCTS), game1 (alpha-beta vs. tree-reusing MCTS)
```

## How to run

```bash
python -m pip install -e .
python -m scripts.game
```

Smoke tests (imports, initial board): `python -m unittest discover -s tests`.

> **Note:** the agents are exploratory implementations. Agent-vs-agent results should not be read as a validated comparison, because move indexing between the MCTS tree and the board still has a known inconsistency.
