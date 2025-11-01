class Player():
    def __init__(self):
        self.__cards = []
        self.__money = 999
        self.__totalGameBet = 0
        self.__inRound = True
        self.__isFolded = False

    def gameReset(self):
        self.__totalGameBet = 0
        self.__inRound = True
        
    def giveCard(self, card):
        # method to give a card to a player
        # input: 2-char string eg "2H"

        # ensure that the hand is not already full
        if len(self.__cards) >= 2:
            raise Exception("Player hand is already full")
        
        # ensure the card is in the valid format, eg 2S, AQ
        if len(card) != 2:
            raise Exception("Please use the valid format for cards")
        
        if card[0] not in "23456789TJQKA" or card[1] not in "HSDC":
            raise Exception("Please use the valid format for cards")
        
        self.__cards.append(card)

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
        # output: True if check is met, False if it is not

        bet_difference = currentPoolRequirement - self.__totalGameBet 
        if bet_difference < 0:
            raise Exception("The player has already bet more than is required for this round")

        if self.__money <= bet_difference:
            # Logic for going all in
            return False
    
        self.__money = self.__money - bet_difference
        return True
    
    def raiseTo(self, betAmount, minibet):

        # logic to check if betAmount is greater than the max bet for this round
        # DOES NOT CURRENTLY WORK
        if betAmount == minibet:
            raise Exception("Cannot raise to the existing bet. Please use Player.check() instead")
        
        if betAmount < minibet:
            raise Exception("Cannot raise to a value less than the existing bet." \
            "Please input something greater than" + str(minibet))
        
        if betAmount > self.__money:
            raise Exception("Player does not have enough money to make this raise")
        
        # ELSE RAISE LOGIC GOES HERE
        self.__money -= betAmount
        return True
    
    def revealBalance(self):
        print("Balance:", self.__money)
    
    def bet(self, minibet):
        # input: minibet - smallest possible bet permissible
        # output: true if successful
        self.revealBalance()
        betAmount = int(input("Stake (minimum " + str(minibet) + "): "))
        if betAmount == -1:
            self.fold()
            return True

        # if bet is too large for balance or too small to match
        while betAmount > self.__money or betAmount < minibet:
            betAmount = int(input("Bet error! Stake (minimum " + str(minibet) + "): "))

        if betAmount == minibet:
            if self.check(minibet):
                return betAmount
            else:
                print("Player has gone all in!")
        else:
            if self.raiseTo(betAmount, minibet):
                return betAmount
        
        raise Exception()
    
    def fold(self):
        self.__isFolded = True

    def isFolded(self):
        return self.__isFolded
    
    def roundPass(self): 
        # special function to run in a round after a player has gone all-in and now has no choices for the rest of the game
        pass