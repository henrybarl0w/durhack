class Player():
    def __init__(self):
        self.__cards = []
        self.__money = 999
        self.__totalGameBet = 0
        self.__inGame = True
        self.__isFolded = False
        self.__totalRoundBet = 0
        self.__isAllIn = False

    def totalGameBet(self):
        return self.__totalGameBet
    
    def roundReset(self):
        self.__totalRoundBet = 0
        # REQUEST: CALL Player.roundReset() after every round in Dealer.betting()

    def addToRoundBet(self, nAmount):
        self.__totalRoundBet += nAmount
        self.__totalGameBet += nAmount

    def isAllIn(self):
        return self.__isAllIn

    def gameReset(self):
        self.__totalGameBet = 0
        self.__inGame = True
        self.roundReset()
        
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
            self.addToRoundBet(self.__money)
            self.__money = 0
            self.__isAllIn = True
            return "allin"
    
        self.__money = self.__money - bet_difference
        self.__totalGameBet += bet_difference
        return "checkok"
    
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
        self.__totalGameBet += betAmount
        return True
    
    def revealBalance(self):
        print("Balance:", self.__money)

    def revealExistingBet(self):
        print("Existing bet for this round:", self.__totalRoundBet)
    
    def bet(self, minibet):
        # input: minibet - smallest possible bet permissible
        # output: true if successful
        self.revealBalance()
        self.revealExistingBet()
        if minibet < self.__money and self.__money != 0:
            self.check(minibet) # go all in

        print("Current bet: " + str(self.__totalRoundBet))
        betAmount = input("Stake (minimum " + str(minibet) + "): ")
        is_int_amount = False

        while not is_int_amount:
            try: 
                betAmount = int(betAmount)
                is_int_amount = True
            except:
                betAmount = input("Please input an integer! Stake: ")

        if betAmount == -1:
            self.fold()
            return True

        # if bet is too large for balance or too small to match
        while betAmount > self.__money or betAmount < minibet:
            betAmount = int(input("Bet error! Stake (minimum " + str(minibet) + "): "))

        # if they are checking (updating their bet to the same as the minimum for this round)
        if betAmount == minibet:
            match self.check(minibet):
                case "checkok":
                    return betAmount
                case "allin":
                    print("Player has gone all in!")
                    self.__isAllIn = True
                    return self.__totalGameBet
        else:
            if self.raiseTo(betAmount, minibet):
                self.addToRoundBet(betAmount)
                return betAmount
        
        raise Exception()
    
    def totalGameBet(self):
        return self.__totalGameBet
    
    def fold(self):
        self.__isFolded = True

    def isFolded(self):
        return self.__isFolded
    
    def roundPass(self): 
        # special function to run in a round after a player has gone all-in and now has no choices for the rest of the game
        pass