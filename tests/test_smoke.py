from pathlib import Path
import ast, importlib, unittest
ROOT = Path(__file__).resolve().parents[1]
class SmokeTests(unittest.TestCase):
    def test_python_compiles(self):
        for directory in ['src','scripts']:
            for f in (ROOT/directory).rglob('*.py'):compile(f.read_text(encoding='utf-8-sig'),str(f),'exec')

    def test_imports_without_starting_games(self):
        import mancala_ai.mcts, mancala_ai.mcts_variant, mancala_ai.minimax
        import scripts.game, scripts.game1
        from mancala_ai.rules import make_board
        b=make_board()
        self.assertEqual(len(b),14)
        self.assertEqual(int(b.sum()),48)

if __name__ == '__main__':unittest.main()
