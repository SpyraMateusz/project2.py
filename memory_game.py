# Plik memory_game.py

import random

class MemoryGame:
    def __init__(self, size=4):
        self.size = size
        self.board = self.generate_board()
        self.revealed = [[False] * size for _ in range(size)]
        self.moves = 0

    def generate_board(self):
        num_pairs = (self.size * self.size) // 2
        values = list(range(num_pairs)) * 2
        random.shuffle(values)
        return [values[i:i + self.size] for i in range(0, len(values), self.size)]

    def display_board(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.revealed[row][col]:
                    print(f"{self.board[row][col]:2}", end=" ")
                else:
                    print("X ", end=" ")
            print()

    def make_move(self, x1, y1, x2, y2):
        self.moves += 1
        if self.board[x1][y1] == self.board[x2][y2]:
            self.revealed[x1][y1] = self.revealed[x2][y2] = True
            return True
        return False

    def is_finished(self):
        return all(all(row) for row in self.revealed)

def get_coordinates():
    try:
        x, y = map(int, input("Enter coordinates (row col): ").split())
        return x, y
    except ValueError:
        print("Invalid input. Please enter two numbers separated by a space.")
        return get_coordinates()

def main():
    game = MemoryGame()
    while not game.is_finished():
        game.display_board()
        x1, y1 = get_coordinates()
        x2, y2 = get_coordinates()
        if not game.make_move(x1, y1, x2, y2):
            print("No match. Try again.")
    game.display_board()
    print(f"Congratulations! You completed the game in {game.moves} moves.")

if __name__ == "__main__":
    main()