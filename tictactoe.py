#! /usr/bin/env python3
# coding=utf-8
"""
A simple command-line Tic-Tac-Toe game.

 x | o | x
---+---+---
 o | x | o
---+---+---
 x |   |

Table with VT100 Excape Sequences: http://ascii-table.com/ansi-escape-sequences-vt-100.php
"""
import itertools

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"
__date__ = "2014-11-18"

# VT100 escape sequences for cursor and screen manipulation
HIDE_CUR = "\x1b[?25l"
SHOW_CUR = "\x1b[?25h"
CLEAR = "\x1b[2K"
MOVE_UP = "\x1b[1A"
MOVE_START = "\x1b[0G"


class TicTacToe:
    """
    Represents the logic for a Tic-Tac-Toe game.
    """
    def __init__(self):
        """Initializes the game board."""
        self.field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def check_win(self):
        """
        Checks if a player has won the game.

        Returns:
            bool: True if a player has won, False otherwise.
        """
        transposed_field = [[self.field[col][row] for col in range(3)] for row in range(3)]
        ldiag_field = [[self.field[col][col] for col in range(3)]]
        rdiag_field = [[self.field[col][2 - col] for col in range(3)]]
        fields = self.field + transposed_field + ldiag_field + rdiag_field

        return any(f in [["x", "x", "x"], ["o", "o", "o"]] for f in fields)

    def is_full(self):
        """
        Checks if the board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        return all(cell != " " for row in self.field for cell in row)

    def make_move(self, pos, player):
        """
        Makes a move on the board.

        Args:
            pos (int): The position to move to (1-9).
            player (str): The player making the move ('x' or 'o').

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        if 1 <= pos <= 9 and self.field[(pos - 1) // 3][(pos - 1) % 3] == " ":
            self.field[(pos - 1) // 3][(pos - 1) % 3] = player
            return True
        return False


def display_field(field, clear=True):
    """
    Displays the game board on the console.

    Args:
        field (list): The game board.
        clear (bool): Whether to clear the console before printing.
    """
    if clear:
        print(HIDE_CUR + CLEAR + (MOVE_UP + CLEAR) * 6 + MOVE_START, end="")
    print(HIDE_CUR + " " + " \n---+---+---\n ".join(" | ".join(row) for row in field) + " " + SHOW_CUR)


def play_game():
    """
    Starts and manages a single game of Tic-Tac-Toe.
    """
    game = TicTacToe()
    display_field(game.field, clear=False)

    player_cycle = itertools.cycle(["x", "o"])
    current_player = next(player_cycle)

    while True:
        pos = input(f"Player {current_player}: Enter a position (1-9): ")
        if not pos.isdigit() or not (1 <= int(pos) <= 9):
            print(MOVE_UP + CLEAR + MOVE_START + "Invalid input. Please enter a number between 1 and 9.", end="")
            continue

        pos = int(pos)
        if not game.make_move(pos, current_player):
            print(MOVE_UP + CLEAR + MOVE_START + "Position already taken. ", end="")
        else:
            display_field(game.field)
            if game.check_win():
                print(f"Player {current_player} won!")
                break
            if game.is_full():
                print("It's a draw!")
                break
            current_player = next(player_cycle)


def main():
    """
    Main function to run the Tic-Tac-Toe game and ask for replays.
    """
    while True:
        play_game()
        again = input("Play again? (y) ")
        if again.lower() != "y":
            break


if __name__ == "__main__":
    main()