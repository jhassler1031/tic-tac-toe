
import random

class Position:
     def __init__(self):
         self.mark = " "

     def __repr__(self):
         return self.mark

"""
     def is_open(self):
         if self.mark == " ":
             return True
         else:
             return False
"""

class Board:
    def __init__(self):
        self.board = []
        self.size = 3

        for row in range(self.size):
            row = []
            for col_count in range(self.size):
                row.append(Position())

            self.board.append(row)

    def __str__(self):
        r_count = 0
        c_count = 0
        print("  0  " "  1  " "  2  ")
        for row in self.board:
            print(str(r_count) + " ", end = "")

            for col in row:
                print(col, end = " ")
                if c_count != self.size - 1:
                    print(" | ", end = "")
                c_count += 1

            c_count = 0
            print("")
            if r_count != self.size -1:
                print("---------------")
            r_count += 1
        return ""

    def game_over(self):
        new_list = []
        r_idx = 0
        c_idx = 0
        for _ in range(self.size):
            new_list.append([])

        for row in self.board:
            c_idx = 0
            for col in row:
                new_list[r_idx].append(str(self.board[r_idx][c_idx].mark))
                c_idx += 1
            r_idx += 1
        print(new_list)

    def turn(self, player):
        row = None
        col = None

        while True:
            print(f"It's {player}'s turn.")

            player_input = input("Please enter the row number and column number you wish to play, separated by a space: ")
            player_input = player_input.lower()
            player_input = player_input.split()

            row = int(player_input[0])
            col = int(player_input[1])
            if (row >= 0 and row <=self.size - 1) and (col >= 0 and col <= self.size -1):
                if self.board[row][col].mark == " ":
                    if player == "Player X":
                        self.board[row][col].mark = "X"
                    else:
                        self.board[row][col].mark = "O"
                    break
                else:
                    print("I'm sorry, that position has already been taken.")

            else:
                print("I'm sorry, that's not a valid entry.  Example, to play in row 0 column 0, enter: 0 0")










#Start of program

player_x = "Player X"
player_o = "player O"

game = Board()
x=0
"""
for _ in range(6):
    print(game)
    if x % 2 == 0:
        game.turn(player_x)
    else:
        game.turn(player_o)
    x += 1
"""
game.game_over()
