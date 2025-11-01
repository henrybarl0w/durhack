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
        for player in self.players:
            player.giveCard()
        pass

    # Deals with a round of betting and shows n number of cards at the start
    def betting(self, n):
        pass

class Player():
    def __init__(self):
        self.__cards = []
        self.__money = 0
        self.__totalGameBet = 0

    def gameReset(self):
        self.__totalGameBet = 0
        

    def giveCard(self, card):
        # method to give a card to a player
        # input: 2-char string eg "2H"

        # ensure that the hand is not already full
        if len(self.__cards) >= 2:
            raise Exception("Player hand is already full")
        
        # ensure the card is in the valid format, eg 2S, AQ
        if len(card) != 2:
            raise Exception("Please use the valid format for cards")
        if (card[0] not in "23456789JQKA") or (card[1] not in "HSDC"):
            raise Exception("Please use the valid format for cards")
        
        self.cards.append(card)

    def getCards(self):
        # method to return all private cards a player has in their hand
        return self.__cards
    
    def clearCards(self):
        self.__cards = []
    
    def setMoney(self, nMoney):
        self.__money = nMoney

    def addMoney(self, nMoney):
        self.__money += nMoney

    

    def isBankrupt(self):
        # function to be run at the start of the game for each players
        if self.__money <= 0:
            return True
        return False

    def check(self, currentPoolRequirement):
        # input: current pool bet per person for this round
        #output: True if check is met, False if it is not

        bet_difference = currentPoolRequirement - self.__totalGameBet 
        if bet_difference < 0:
            raise Exception("The player has already bet more than is required for this round")

        if self.__money <= bet_difference:
            # Logic for going all in
            return False
    
        self.__money = self.__money - bet_difference
        return True