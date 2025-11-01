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
        self.pot = 0

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

    def equalBets(self, bets):
        for i in range(bets.count(None)):
            bets.remove(None)
        if len(set(bets)) == 1: return True
        return False

    def betting(self, n):
        # Deals with a round of betting and shows n number of cards at the start

        # Iteratively assign n community cards from the top of the deck
        for i in range(n): # for flop n=3, for turn and river n=1
            self.communityCards.append(self.deck.pop())

        # test that the assignment has worked correctly
        print(self.communityCards) # (this is true, so this line may be removed)

        # set the pointer to the first item in the players list, whom will be dealt to first (little blind)
        index = self.little

        bets = [None for _ in range(len(self.players))]

        # boolean to check that we are still going through the players for the first time
        

        # boolean to check that non-folded players have still not reached a bet consensus for this round
        

        while index < self.little+len(self.players) or not self.equalBets(bets.copy()):
            i = index % len(self.players)
            player = self.players[i]

            if player.isFolded(): 
                continue
            
            print('Player ', index % len(self.players))
            betSize = player.bet(self.minBet)
            if betSize == -1: 
                player.fold()
            elif betSize > self.minBet: 
                self.minBet = betSize
                bets[i] = betSize
            else: 
                bets[i] = betSize
            index += 1

        # Add all bets from this round to the pot
        for bet in bets:
            if bet is not None:
                self.pot += bet
        
        print("Pot size:",self.pot)
        for player in self.players:
            player.roundReset() # tell the player to update its memory of how much it's spent this round to zero (to prepare for next round)

    def orderHand(self, h):
        cardOrder = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        swapped = True
        n = len(h)
        while swapped and n >= 0:
            swapped = False
            for i in range(n-1):
                if cardOrder.index(h[i][0:1]) > cardOrder.index(h[i+1][0:1]):
                    temp = h[i]
                    h[i] = h[i+1]
                    h[i+1] = temp
                    swapped = True
            n -= 1
        return h

    def rankHand(self, h):
        h = self.orderHand(h)
        cardOrder = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        # Check for same suit
        sameSuit = True
        s = h[0][1:2]
        for i in range(1, len(h)):
            if h[i][1:2] != s:
                sameSuit = False
                break
        # Check for consecutive cards 
        consecutive = True
        last = cardOrder.index(h[0][0:1])
        for i in range(1, len(h)):
            current = cardOrder.index(h[i][0:1])
            if current != last + 1:
                consecutive = False
                break
            last = current

        if sameSuit and consecutive:
            if h[4][0:1] == 'A': return (10, 0) #'royal flush'
            return (9, 0) #'straight flush'
        
        # Count repeated cards
        count = [] # [card, count]
        for c in h:
            found = False
            for card in count:
                if c[0:1] in card:
                    card[1] += 1
                    found = True
                    break
            if not found: count.append([c[0:1], 1])

        m = 0
        a, b = 0, 0
        for card in count:
            if card[1] > m:
                m = card[1]
                a = cardOrder.index(card[0])
            if cardOrder.index(card[0]) > b: b = cardOrder.index(card[0])
        if m == 4:
            return (8, 0) #'four of kind'
        
        if m == 3 and (count[0][1] == 2 or count[1][1] == 2):
            return (7, 0) #'full house'
        
        if sameSuit:
            return (6, 0) #'flush'
        
        if consecutive:
            return (5, 0) #'straight'
        
        if m == 3:
            return (4, 0) #'three of kind'
        
        if m == 2:
            pairs = 0
            for i in range(len(count)):
                if count[i][1] == 2: pairs += 1
            if pairs == 2:
                return (3, 0) #'two pairs'
            return (2, a) #'pair'
        return (1, b) #'highest card'

    def draw(self, h1, h2):
        cardOrder = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        h1, h2 = self.orderHand(h1), self.orderHand(h2)
        for i in range(len(h1)-1,-1,-1):
            if h1[i][0:1] != h2[i][0:1]:
                if cardOrder.index(h1[i][0:1]) > cardOrder.index(h2[i][0:1]):
                    return True
                return False
            
    def findBestHand(self):
        bestHands = []
        for player in self.players:
            if player.isFolded(): continue
            cards = player.getCards() + self.communityCards
            hands = []
            for i in range(len(cards)-1):
                for j in range(i+1,len(cards)):
                    hand = []
                    for k in range(len(cards)):
                        if k not in [i,j]:
                            hand.append(cards[k])
                    hands.append(hand)
            bestHand = None
            rank = (0, 0)
            for hand in hands:
                a, b = self.rankHand(hand)
                if a > rank[0] or (a == rank[0] and (b > rank[1] or (b == rank[1] and self.draw(hand, bestHand)))):
                    rank = (a, b)
                    bestHand = hand
            bestHands.append(bestHand)

        # Finds the best hand out of each players best hand
        bestHand = None
        rank = (0, 0)
        for hand in bestHands:
            a, b = self.rankHand(hand)
            if a > rank[0] or (a == rank[0] and (b > rank[1] or (b == rank[1] and self.draw(hand, bestHand)))):
                rank = (a, b)
                bestHand = hand
                
        return bestHands.index(bestHand)