# Durhack 2025
import dealer, player

def generateDeck():
    # function to generate a list that will store every possible card in the deck
    suits = ['H','S','D','C']
    values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    deck = []
    for suit in suits:
        for value in values:
            deck.append(value + suit)
    return deck

INITIALMONEY = 1000 # initial amount of money each player should have

game = dealer.Dealer() # initialize a game state

# create a list of n (here 4) players, stored by Player class and players list of objects
for _ in range(4): 
    game.players.append(player.Player())

# assign each player the decided amount of money
for i in range(len(game.players)):
    (game.players)[i].setMoney(INITIALMONEY)

print("AAAAAAAAAAAA", game.players[0].getMoney())
# deal the cards to each player
game.deal()

# display the cards of each player to the screen
for i in range(4): 
    print(game.players[i].getCards())

# start the pre-flop betting (0 = preflop, 3 = flop, 4 = turn, 5 = river)
#game.betting(0)

game.betting(5)
winner = game.findBestHand()
game.players[winner].addMoney(game.pot)

for p in game.players:
    print(p.getMoney())
