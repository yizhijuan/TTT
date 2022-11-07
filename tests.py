import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        board = [
            ['X', 'O', 'X'],
            [None, 'O', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')
    # TODO: Test all functions from logic.py!


if __name__ == '__main__':
    unittest.main()