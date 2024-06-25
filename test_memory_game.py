# Plik test_memory_game.py

import unittest
from memory_game import MemoryGame

class TestMemoryGame(unittest.TestCase):
    def test_initialization(self):
        game = MemoryGame(4)
        self.assertEqual(len(game.board), 4)
        self.assertEqual(len(game.board[0]), 4)

    def test_make_move(self):
        game = MemoryGame(4)
        game.board = [
            [0, 0, 1, 1],
            [2, 2, 3, 3],
            [4, 4, 5, 5],
            [6, 6, 7, 7]
        ]
        self.assertTrue(game.make_move(0, 0, 0, 1))
        self.assertFalse(game.make_move(0, 0, 1, 1))

    def test_is_finished(self):
        game = MemoryGame(4)
        game.revealed = [[True] * 4 for _ in range(4)]
        self.assertTrue(game.is_finished())

if __name__ == '__main__':
    unittest.main()