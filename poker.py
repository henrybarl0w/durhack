# Durhack 2025
import dealer, player
# Tempory function to generate deck
'''suits = ['H','S','D','C']
values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
deck = []
for suit in suits:
    for value in values:
        deck.append(value + suit)
print(deck)'''

# Test
INITIALMONEY = 1000
game = dealer.Dealer()
for _ in range(4): game.players.append(player.Player())
for i in range(len(game.players)):
    (game.players)[i].setMoney(INITIALMONEY)
game.deal()
for i in range(4): print(game.players[i].getCards())
game.betting(0)