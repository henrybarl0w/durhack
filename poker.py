# Durhack 2025
import dealer, player

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
# game.betting(0)

game.betting(3)
game.betting(1)
game.betting(1)
winner = game.findBestHand()
game.players[winner].addMoney(game.pot)

for p in game.players:
    print(p.getMoney())
