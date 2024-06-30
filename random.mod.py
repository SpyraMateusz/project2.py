import random

class CardGame:
    def __init__(self):
        self.cards = ['Ace of Spades', '2 of Hearts', '3 of Diamonds', '4 of Clubs', ...]  # Pełna lista kart
        self.shuffle_cards()

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return "No more cards to draw!"

    def reset_deck(self):
        self.cards = ['Ace of Spades', '2 of Hearts', '3 of Diamonds', '4 of Clubs', ...]  # Zresetowanie listy kart
        self.shuffle_cards()

# Przykładowe użycie
game = CardGame()
print("Shuffled deck: ", game.cards)

# Odkrywanie kart
print("Drawing a card: ", game.draw_card())
print("Remaining cards: ", game.cards)

# Resetowanie talii
game.reset_deck()
print("Reset and shuffled deck: ", game.cards)