class MemoryGame:
    # ... (pozostała część klasy)

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