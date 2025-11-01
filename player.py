class Player:
    def __init__(self):
        self.__cards = []
        self.__money = 0
        self.__betRound = 0      # bet amount in current betting round
        self.__betGame = 0       # cumulative bet in current game
        self.__isFolded = False
        self.__isAllIn = False

    # ------------------------------
    # Game and Round Reset
    # ------------------------------
    def gameReset(self):
        """Resets player state for a new game."""
        self.__betGame = 0
        self.__isFolded = False
        self.__isAllIn = False
        self.__cards.clear()
        self.roundReset()

    def roundReset(self):
        """Resets round-specific betting values."""
        self.__betRound = 0

    def letRoundBetBe(self, n):
        self.__betRound = n

    # ------------------------------
    # Money Management
    # ------------------------------
    def setMoney(self, amount):
        self.__money = amount

    def addMoney(self, amount):
        self.__money += amount

    def getMoney(self):
        return self.__money

    def isBankrupt(self):
        return self.__money <= 0

    # ------------------------------
    # Cards
    # ------------------------------
    def giveCard(self, card):
        if len(self.__cards) >= 2:
            raise Exception("Player hand is already full")

        if len(card) != 2 or card[0] not in "23456789TJQKA" or card[1] not in "HSDC":
            raise Exception("Invalid card format")

        self.__cards.append(card)

    def getCards(self):
        return list(self.__cards)

    # ------------------------------
    # Betting
    # ------------------------------
    def bet(self, minBet):
        """Handles player betting for one turn."""
        if self.__isFolded or self.__isAllIn:
            print("Player cannot act (folded or all-in).")
            return False

        if self.__money == 0:
            print("Player has no money. Automatically passing.")
            return True

        print(f"You have ${self.__money}. Minimum to call is ${minBet}.")
        print("Enter -1 to fold, 0 to call/check, or a positive number to raise:")

        while True:
            try:
                choice = int(input("Your bet: "))
                break
            except ValueError:
                print("Please enter an integer.")

        if choice == -1:
            self.fold()
            print("Player folds.")
            return True

        elif choice == 0:
            # call/check
            betAmount = min(minBet, self.__money)
            self.__money -= betAmount
            self.__betRound += betAmount
            self.__betGame += betAmount
            if self.__money == 0:
                self.__isAllIn = True
            print(f"Player calls with ${betAmount}.")
            return True

        elif choice > 0:
            if choice >= self.__money:
                choice = self.__money
                self.__isAllIn = True
                print("Player goes all-in!")

            self.__money -= choice
            self.__betRound += choice
            self.__betGame += choice
            print(f"Player bets ${choice}.")
            return True

    # ------------------------------
    # Getters for Bets
    # ------------------------------
    def getBetForThisRound(self):
        return self.__betRound

    def getBetForThisGame(self):
        return self.__betGame

    # ------------------------------
    # Fold / All-in
    # ------------------------------
    def fold(self):
        self.__isFolded = True

    def isFolded(self):
        return self.__isFolded

    def isAllIn(self):
        return self.__isAllIn
