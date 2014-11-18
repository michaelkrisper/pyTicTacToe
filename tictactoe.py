#! /usr/bin/env python3
# coding=utf-8
"""
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

HIDE_CUR = "\x1b[?25l"
SHOW_CUR = "\x1b[?25h"
CLEAR = "\x1b[2K"
MOVE_UP = "\x1b[1A"
MOVE_START = "\x1b[0G"


def displayField(field, clear=True):
    if clear:
        print(HIDE_CUR + CLEAR + (MOVE_UP + CLEAR) * 6 + MOVE_START, end="")
    print(HIDE_CUR + " " + " \n---+---+---\n ".join(" | ".join(row) for row in field) + " " + SHOW_CUR)


def checkWin(field):
    transposed_field = [[field[col][row] for col in range(3)] for row in range(3)]
    ldiag_field = [[field[col][col] for col in range(3)]]
    rdiag_field = [[field[col][2 - col] for col in range(3)]]
    fields = field + transposed_field + ldiag_field + rdiag_field

    return any(f in [["x", "x", "x"], ["o", "o", "o"]] for f in fields)


def play():
    field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    displayField(field, clear=False)

    player = itertools.cycle(["x", "o"])
    p = next(player)
    pos = input("Player {}: Enter a position (1-9): ".format(p))
    while "1" <= pos <= "9":
        pos = int(pos)
        if field[(pos - 1) // 3][(pos - 1) % 3] != " ":
            print(MOVE_UP + CLEAR + MOVE_START + "Position already taken. ", end="")
        else:
            field[(pos - 1) // 3][(pos - 1) % 3] = p
            displayField(field)
            if checkWin(field):
                print("Player {} won!".format(p))
                return
            p = next(player)

        pos = input("Player {}: Enter a position (1-9): ".format(p))


def main():
    play()
    again = input("Play again ? (y) ")
    while again.lower() == "y":
        play()
        again = input("Play again? (y) ")


if __name__ == "__main__":
    main()