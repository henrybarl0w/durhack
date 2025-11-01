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

# deal the cards to each player
game.deal()


# start the pre-flop betting (0 = preflop, 3 = flop, 4 = turn, 5 = river)

game.betting(5)

winner = game.findBestHand()
game.players[winner].addMoney(game.pot)

for p in game.players:
    print(p.getMoney())
    p.roundReset()

game.reset()
game.deal()
game.betting(5)


winner = game.findBestHand()
game.players[winner].addMoney(game.pot)

for p in game.players:
    print(p.getMoney())
