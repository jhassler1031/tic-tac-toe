
class Position:
     def __init__(self):
         self.mark = " X "

     def __repr__(self):
         return "X"


class Board:
    def __init__(self):
        self.board = []
        self.size = 6

        for row in range(self.size):
            row = []
            for col_count in range(self.size):
                row.append(col_count)

            self.board.append(row)

    def __str__(self):
        for row in self.board:
            for col in row:
                #if row == 0 and col == 1 or col == 3 or col ==5:
                print(col, end = "   ")
            print("")
        return ""




#Start of program

x = Board()
print(x)
