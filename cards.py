import random

class Card:
    SUITS = ['H', 'S', 'D', 'C']  # Hearts, Spades, Diamonds, Clubs
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    def __init__(self, rank, suit):
        if rank not in self.RANKS or suit not in self.SUITS:
            raise ValueError("Invalid card rank or suit")
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return f"Card(rank='{self.rank}', suit='{self.suit}')"


class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards in the deck to deal")
        return [self.cards.pop() for _ in range(num_cards)]


def main():
    deck = Deck()
    print("Deck shuffled. Cards in the deck:")
    print(deck.cards)

    dealt_cards = deck.deal(5)
    print("Dealt cards:")
    print(dealt_cards)


if __name__ == "__main__":
    main()