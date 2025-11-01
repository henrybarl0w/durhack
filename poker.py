# Durhack 2025

# Tempory function to generate deck
'''suits = ['H','S','D','C']
values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
deck = []
for suit in suits:
    for value in values:
        deck.append(value + suit)
print(deck)'''




# Test
game = Dealer()
for _ in range(4): game.players.append(Player())
game.deal()
for i in range(4): print(game.players[i].getCards())
game.betting(0)