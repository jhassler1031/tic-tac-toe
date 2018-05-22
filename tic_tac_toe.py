
import random

class Position:
     def __init__(self):
         self.mark = " "

     def __repr__(self):
         return self.mark

     def change_mark(self, player):
         if player == "computer":
             self.mark = "O"
         else:
             self.mark = "X"

     def is_open(self):
         if self.mark == " ":
             return True
         else:
             return False


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

    def human_turn(self):
        row = None
        col = None

        while True:
            player_input = input("Please enter the row number and column number you wish to play, separated by a space: ")
            player_input = player_input.lower()
            player_input = player_input.split()

            row = int(player_input[0])
            col = int(player_input[1])
            if (row >= 0 and row <=self.size - 1) and (col >= 0 and col <= self.size -1):
                break
            else:
                print("I'm sorry, that's not a valid entry.  Example, to play in row 0 column 0, enter: 0 0")




    def computer_turn(self):
        pass










#Start of program

x = Board()
print(x)
x.human_turn()
