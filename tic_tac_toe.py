
class Position:
     def __init__(self):
         self.mark = " X "

     def __repr__(self):
         return "X"


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




#Start of program

x = Board()
print(x)
