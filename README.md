# MancalaAI

Install Python 3.11+ and `python -m pip install -e .`. From the repository root run `python -m scripts.game`. Commands execute experiments or launch the application; importing the model package is separate.

See [layout](docs/layout.md) and [file migration](docs/file-migration.json). Source implementations, author attribution in supplied reports and distinct historical variants are retained. New figure/table outputs are routed to results/generated. Dependency declarations describe imports, not a reconstruction of the original historical environment. No new licence is assigned.

## Current limitations

Gameplay and agent logic are intentionally unchanged, including the previously identified action-13 and MCTS move-mapping issues. Simulations should not be treated as validated comparisons of agents. This task only reorganizes files and prevents games from starting merely on import.

## Checks

`python -m unittest discover -s tests -v` runs migration checks. Full financial experiments, agent tournaments and GUI sessions were not rerun.
