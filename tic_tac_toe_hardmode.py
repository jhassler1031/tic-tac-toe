
import random

#Start of Position class

class Position:
     def __init__(self):
         self.mark = " "

     def __repr__(self):
         return self.mark


#Start of Board class

class Board:

#__init__ method

    def __init__(self):
        self.board = []
        self.size = 3

        for row in range(self.size):
            row = []
            for col_count in range(self.size):
                row.append(Position())

            self.board.append(row)

#__str__ method

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

#game over method

    def game_over(self, player):
        new_list = []
        columns = []
        diagonal = [["", "", ""], ["", "", ""]]
        r_idx = 0
        c_idx = 0
        draw = 0
        for _ in range(self.size):
            new_list.append([])

        #Builds lists for easy checking
        for row in self.board:
            c_idx = 0
            for col in row:
                new_list[r_idx].append(str(self.board[r_idx][c_idx].mark))
                if r_idx == 0:
                    if c_idx == 0:
                        diagonal[0].append(str(self.board[r_idx][c_idx].mark))
                    elif c_idx == 2:
                        diagonal[1].append(str(self.board[r_idx][c_idx].mark))
                elif r_idx == 1:
                    if c_idx == 1:
                        diagonal[0].append(str(self.board[r_idx][c_idx].mark))
                        diagonal[1].append(str(self.board[r_idx][c_idx].mark))
                else:
                    if c_idx == 0:
                        diagonal[1].append(str(self.board[r_idx][c_idx].mark))
                    elif c_idx == 2:
                        diagonal[0].append(str(self.board[r_idx][c_idx].mark))
                c_idx += 1
            r_idx += 1


        for row in self.board:
            columns.append([])

        #Begin checks for win

        for row in new_list:
            if row.count("X") == 3 or row.count("O") == 3:
                print(f"{player} has won the game!")
                return True
            draw += row.count(" ")
            columns[0].append(row[0])
            columns[1].append(row[1])
            columns[2].append(row[2])

        #Check for a draw
        if draw == 0:
            print("It's a draw")
            return True

        for row in columns:
            if row.count("X") == 3 or row.count("O") == 3:
                print(f"{player} has won the game!")
                return True

        for row in diagonal:
            if row.count("X") == 3 or row.count("O") == 3:
                print(f"{player} has won the game!")
                return True

        return False

#start of turn method

    def turn(self, player):
        row = None
        col = None

        while True:
            print(f"It's {player}'s turn.")

            player_input = input("Please enter the row number and column number you wish to play, separated by a space: ")
            if player_input != "" and len(player_input) > 2 and len(player_input) < 4:
                player_input = player_input.lower()
                player_input = player_input.split()

                if player_input[0].isdigit() and player_input[1].isdigit():

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

"""
player_x = "Player X"
player_o = "player O"
current_player = ""
"""

players = ["Player X", "Player O"]
counter = 0

game = Board()
x=0

print(game)

while True:
    """
    if x % 2 == 0:
        current_player = player_x
    else:
        current_player = player_o
    """
    current_player = players[counter]
    game.turn(current_player)
    print(game)
    if game.game_over(current_player):
        break
    counter = int(not counter)
    #x += 1
