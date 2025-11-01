class Player():
    def __init__(self):
        self.__cards = []
        self.__money = 0
        self.__totalGameBet = 0
        self.__isFolded = False
        self.__isAllIn = False
        self.__roundStartMoney = 0
        self.__hasPlayedThisRound = False

    def roundReset(self):
        self.__roundStartMoney = self.__money
        # REQUEST: CALL Player.roundReset() after every round in Dealer.betting()

    def letRoundBetBe(self, nAmount):
        self.__totalRoundBet = nAmount

    def hasPlayedThisRound(self):
        self.__hasPlayedThisRound = True


    def getBetForThisRound(self):
        return self.__totalRoundBet

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
        self.__roundStartMoney = nMoney

    def getMoney(self):
        return self.__money

    def addMoney(self, nMoney):
        self.__money += nMoney

    def isBankrupt(self):
        # function to be run at the start of the game for each players
        if self.__money <= 0:
            return True
        return False

    def bet(self, minibet):
        # input:  minimum bet permissible for this turn
        # output: True if successful

        # Case I: not able to bet for this round; do nothing
        if self.__money == 0:
            print("Player has no money. Automatically passing")
            return True

        # Case II: has money but not enough; offer fold or all-in
        elif self.__money <= minibet:
            print("You have", self.__money, "but you need",minibet)
            print("You have the option to go ALL IN")
            print("In this case you will double your money if you win this round, or be bust if you lose it")
            print("You also have the choice of folding, in which case you will be out of this round but retain your money")
            print("Do you Fold (-1) or go All-in (0)? ")
            print()
            choice = input("Turn: ")
            while choice != "-1" and choice != "0":
                choice = input("Turn: ")
            
            if choice == "-1":
                # folding logic
                pass

            elif choice == "0":
                # all-in logic
                pass

        # Case III: has more money than needed 
        elif self.__money > minibet:

            choiceMade = False
            while not choiceMade:
                try:
                    choice = int(input("Turn: "))
                except:
                    print("Must be an integer")

            # check
            if choice == 0:
                # do nothing
                pass
            

            elif choice == -1:
                # folding logic
                pass

            elif choice > 0 and choice < self.__money:
                # raise
                pass

            elif choice > 0 and choice > self.__money:
                print("More money offered than available. Offering everything")
                # all-in logic
                
    
    def totalGameBet(self):
        return self.__totalGameBet
    
    def fold(self):
        self.__isFolded = True

    def isFolded(self):
        return self.__isFolded
    
    def roundPass(self): 
        # special function to run in a round after a player has gone all-in and now has no choices for the rest of the game
        pass