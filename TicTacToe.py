class Field:
    def __init__(self):
        self.field = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def print_field(self):
        print(self.field[0][0] + " | " + self.field[0][1] + " | " + self.field[0][2] + "\n" +
              self.field[1][0] + " | " + self.field[1][1] + " | " + self.field[1][2] + "\n" +
              self.field[2][0] + " | " + self.field[2][1] + " | " + self.field[2][2])

    def clear(self):
        for a in range(len(self.field) - 1):
            for b in range(len(self.field[a]) - 1):
                self.field[a][b] = "-"

    def set(self, index, replacement):
        if replacement == "X" or replacement == "O":
            if index.isdigit():
                index = int(index) - 1
                if 0 <= index <= 2:
                    if self.field[0][index] == "-":
                        self.field[0][index] = replacement
                elif 3 <= index <= 5:
                    if self.field[1][index - 3] == "-":
                        self.field[1][index - 3] = replacement
                elif 6 <= index <= 8:
                    if self.field[2][index - 6] == "-":
                        self.field[2][index - 6] = replacement


class Win:
    def check_win(self):
        for player in ["X", "O"]:
            if (field.field[0][0] == player) and (field.field[0][1] == player) and (field.field[0][2] == player):
                return player
            elif (field.field[1][0] == player) and (field.field[1][1] == player) and (field.field[1][2] == player):
                return player
            elif (field.field[2][0] == player) and (field.field[2][1] == player) and (field.field[2][2] == player):
                return player
            elif (field.field[0][0] == player) and (field.field[1][0] == player) and (field.field[2][0] == player):
                return player
            elif (field.field[0][1] == player) and (field.field[1][1] == player) and (field.field[2][1] == player):
                return player
            elif (field.field[0][2] == player) and (field.field[1][2] == player) and (field.field[2][2] == player):
                return player
            elif (field.field[0][0] == player) and (field.field[1][1] == player) and (field.field[2][2] == player):
                return player
            elif (field.field[0][2] == player) and (field.field[1][1] == player) and (field.field[2][0] == player):
                return player

    def print_win(self):
        check_win = self.check_win()
        if check_win is not None:
            print("Player " + check_win + " won.")
            exit(0)


if __name__ == "__main__":
    field = Field()
    win = Win()
    field.clear()

    active_player = "X"
    while True:
        field.print_field()
        win.print_win()
        field.set(input("Active Player: " + active_player + "\nField (1 to 9): "), active_player)
        if active_player == "X":
            active_player = "O"
        elif active_player == "O":
            active_player = "X"
