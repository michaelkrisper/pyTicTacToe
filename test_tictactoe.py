import unittest
from tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    """
    Unit tests for the TicTacToe class.
    """

    def setUp(self):
        """
        Set up a new TicTacToe game before each test.
        """
        self.game = TicTacToe()

    def test_initial_board(self):
        """
        Test that the board is initialized correctly.
        """
        expected_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.assertEqual(self.game.field, expected_board)

    def test_make_move(self):
        """
        Test that a move is made correctly.
        """
        self.assertTrue(self.game.make_move(1, "x"))
        self.assertEqual(self.game.field[0][0], "x")

    def test_make_invalid_move(self):
        """
        Test that an invalid move is not allowed.
        """
        self.game.make_move(1, "x")
        self.assertFalse(self.game.make_move(1, "o"))

    def test_check_win_horizontal(self):
        """
        Test for a horizontal win.
        """
        self.game.field[0] = ["x", "x", "x"]
        self.assertTrue(self.game.check_win())

    def test_check_win_vertical(self):
        """
        Test for a vertical win.
        """
        self.game.field[0][0] = "x"
        self.game.field[1][0] = "x"
        self.game.field[2][0] = "x"
        self.assertTrue(self.game.check_win())

    def test_check_win_diagonal(self):
        """
        Test for a diagonal win.
        """
        self.game.field[0][0] = "x"
        self.game.field[1][1] = "x"
        self.game.field[2][2] = "x"
        self.assertTrue(self.game.check_win())

        self.game.field[0][0] = " "
        self.game.field[1][1] = " "
        self.game.field[2][2] = " "

        self.game.field[0][2] = "o"
        self.game.field[1][1] = "o"
        self.game.field[2][0] = "o"
        self.assertTrue(self.game.check_win())

    def test_is_full(self):
        """
        Test that the board is full.
        """
        self.game.field = [["x", "o", "x"], ["o", "x", "o"], ["o", "x", "o"]]
        self.assertTrue(self.game.is_full())

    def test_no_win(self):
        """
        Test that there is no win.
        """
        self.game.field = [["x", "o", "x"], ["o", "x", "o"], ["o", " ", "o"]]
        self.assertFalse(self.game.check_win())

if __name__ == "__main__":
    unittest.main()
