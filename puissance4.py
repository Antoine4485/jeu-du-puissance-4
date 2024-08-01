import random
from os import system, name


class Puissance4:
    NB_ROWS = 6
    NB_COLUMNS = 7
    NB_TOKENS = 4  # nb jetons pour gagner

    def __init__(self):
        self._players = ("X", "O")
        self._ind = 0
        self._grid = []
        while True:
            if not self._play():
                return

    def _play(self) -> bool:
        self._ind = random.randrange(2)
        self._grid = [["" for _ in range(self.NB_COLUMNS)] for _ in range(self.NB_ROWS)]

        while True:
            self._show_game()

            game_over = False
            if (winner := self._get_winner()) != "":
                print(f"Jeu terminé. Le joueur {winner} a gagné.\n")
                game_over = True
            elif self._is_grid_full():
                game_over = True
                print("Jeu terminé. Pas de vainqueur.\n")

            if game_over:
                rep = input("Nouvelle partie (o/n) ? ")
                if rep.lower() == "o":
                    return True
                return False

            # changement de joueur
            self._ind = 1 if self._ind == 0 else 0

            column_num = input(f"Tour du joueur {self._players[self._ind]}. Entrez un numéro de colonne : ")
            print("\n")
            if column_num.lower() == "q":
                return False
            try:
                column_num = int(column_num)
                if (column_num not in range(1, self.NB_COLUMNS + 1) or
                        not self._add_token(self._players[self._ind], column_num - 1)):
                    continue
            except ValueError:
                continue

    def _add_token(self, player, column_num) -> bool:
        for row in reversed(self._grid):
            if row[column_num] == "":
                row[column_num] = player
                return True
        return False

    def _show_game(self):
        self._clear_screen()
        graph = "\n"
        for row in self._grid:
            for cell in row:
                graph += f"|{cell:1}"
            graph += "|\n"
        for j in range(self.NB_COLUMNS):
            graph += " " + str(j + 1)
        print(graph + "\n")

    def _is_grid_full(self) -> bool:
        for row in self._grid:
            if "" in row:
                return False
        return True

    def _get_winner(self) -> str:
        # vérif lignes
        for i in range(self.NB_ROWS):
            for j in range(self.NB_COLUMNS - self.NB_TOKENS + 1):
                if self._grid[i][j] != "" and self._grid[i][j] == self._grid[i][j + 1] == self._grid[i][j + 2] == \
                        self._grid[i][j + 3]:
                    return self._grid[i][j]

        # vérif colonnes
        for j in range(self.NB_COLUMNS):
            for i in range(self.NB_ROWS - self.NB_TOKENS + 1):
                if self._grid[i][j] != "" and self._grid[i][j] == self._grid[i + 1][j] == self._grid[i + 2][j] == \
                        self._grid[i + 3][j]:
                    return self._grid[i][j]

        # vérif diagonale qui va vers la droite et en bas
        for i in range(self.NB_ROWS - self.NB_TOKENS + 1):
            for j in range(self.NB_COLUMNS - self.NB_TOKENS + 1):
                if self._grid[i][j] != "" and self._grid[i][j] == self._grid[i + 1][j + 1] == \
                        self._grid[i + 2][j + 2] == self._grid[i + 3][j + 3]:
                    return self._grid[i][j]

        # vérif diagonale qui va vers la gauche et en bas
        for i in range(self.NB_ROWS - self.NB_TOKENS + 1):
            for j in range(self.NB_COLUMNS - 1, self.NB_COLUMNS - self.NB_TOKENS - 1, -1):
                if self._grid[i][j] != "" and self._grid[i][j] == self._grid[i + 1][j - 1] == \
                        self._grid[i + 2][j - 2] == self._grid[i + 3][j - 3]:
                    return self._grid[i][j]

        return ""

    @staticmethod
    def _clear_screen():
        system("cls") if name == "nt" else system("clear")


if __name__ == '__main__':
    Puissance4()