# game functions

import random
NCARDS = 52

def shuffle_deck(d):
    # function to shuffle the deck d
    return random.shuffle(d)

def deal(nPlayers, deck):

    # check that the number of players is suitable for the number of cards
    if nPlayers > (NCARDS-5)//2:
        raise Exception("Too many players")
    
    