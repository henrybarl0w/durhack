import random

class Dealer():
    def __init__(self):
        self.deck = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH', 
            '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS', 
            '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD', 
            '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC']
        self.players = []
        self.communityCards = []
        self.little = 0
        self.minBet = 5

    def reset(self):
        for player in self.players:
            player.clearCards()
        self.communityCards = []
        self.deck = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH', 
            '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS', 
            '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD', 
            '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC']
        self.minBet = 5

    # Deal two cards to every player
    def deal(self):
        random.shuffle(self.deck)
        for _ in range(2): 
            for player in self.players: player.giveCard(self.deck.pop())

    # Deals with a round of betting and shows n number of cards at the start
    def betting(self, n):
        for i in range(n):
            self.communityCards.append(self.deck.pop())
        #for i in range(self.little, self.little+len(self.players)):
        count = 0
        index = self.little
        while index < self.little+len(self.players) and count != len(self.players) - 1:
            player = self.players[index % len(self.players)]
            if not player.isFolded(): 
                betSize = player.bet(self.minBet)
            if betSize == -1: 
                player.fold()
            elif betSize > self.minBet: 
                self.minBet = betSize
                count = 0
            elif betSize == self.minBet: 
                count += 1