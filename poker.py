# Durhack 2025
import random
# Tempory function to generate deck
'''suits = ['H','S','D','C']
values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
deck = []
for suit in suits:
    for value in values:
        deck.append(value + suit)
print(deck)'''

class Dealer():
    def __init__(self):
        self.deck = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH', 
                '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS', 
                '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD', 
                '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC']
        self.players = []
        self.communityCards = []

    # Deal two cards to every player
    def deal(self):
        random.shuffle(self.deck)
        for _ in range(2): 
            for player in self.players: player.giveCard(self.deck.pop())
        pass

    # Deals with a round of betting and shows n number of cards at the start
    def betting(self, n):
        pass


# Test
game = Dealer()
for _ in range(4): game.players.append(Player())
game.deal()
for i in range(4): print(game.players[i].getCards())
