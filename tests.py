import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board1 = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        board2 = [
            ['X', 'O', 'X'],
            [None, 'O', None],
            [None, 'O', 'X'],
        ]
        board3 = [
            ['X', 'X', 'X'],
            ['2', 'O', 'O'],
            ['O', 'O', 'X'],
        ]
        board4 = [
            ['O', 'X', 'X'],
            ['X', 'X', 'O'],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(logic.get_winner(board1), 'X')
        self.assertEqual(logic.get_winner(board2), 'O')
        self.assertEqual(logic.get_winner(board3), 'X')
    
    # TODO: Test all functions from logic.py!


if __name__ == '__main__':
    unittest.main()