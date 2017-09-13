# Function scores the combination of cards according to the rules of
# Chinese Poker
#
# Inputs:   cards:      list with 13 elements
#                       each element consists of a tuple (value, suit)
#                       The list is divided as follows:
#                           0:4:    Bottom combination
#                           5:9:    Middle combination
#                           10:12:  Top combination
#
# ##################### SCORING ########################
# Bottom combination:
#   straight (2), flush (4), full house (6), poker (10),
#   straight flush (15), royal flush (25)
# Middle combination:
#   three of a kind (2), straight (4), flush (8), full house (16), poker (20),
#   straight flush (30), royal flush (50)
# Top combination:
#   one pair 66 (1), one pair JJ (6), one pair AA (9),
#   three of a kind:
#       222 (10), 777 (15), JJJ (19), AAA (22)

import itertools
import random
import numpy as np
from time import time as tic
from collections import Counter

# Function scores the 13-cards hand
def scoreHand(cards):
    # Break the hand in the individual hands
    bottomHand = sorted(cards[:5], key=lambda card: card[0], reverse=True)
    middleHand = sorted(cards[5:10], key=lambda card: card[0], reverse=True)
    topHand = sorted(cards[10:], key=lambda card: card[0], reverse=True)

    hand = bottomHand

    print(hand)
    scoreSetting(hand)


def scoreSetting(cards):
    # Retrieve array of values and array of suits
    values = [card[0] for card in cards]
    suits = [card[1] for card in cards]
    valuesFrequency = Counter(values).most_common()     # Cards frequency

    # Use an ID to identify the hands:
    #   High Card (1), Pair (2), Two Pairs (3), Three of a Kind (4),
    #   Straight (5), Flush (6), Full House (7), Poker (8),
    #   Straight Flush (9), Royal Flush (10)
    haveStraight, maxValue = getStraight(values)
    print(haveStraight)
    print(maxValue)

###################### CHECK SUB-COMBINATIONS ################################
# Assumption that a combination is made up of maximum 5 cards

# Return the Pairs cards
def getPairs(values):
    pairs = [x for x, y in values if y == 2]
    if not pairs:
        return False, []
    else:
        return True, sorted(pairs, reverse=True)

# Return the Three of a Kind cards
def getThreeOfAKind(values):
    threeOfAKind = [x for x, y in values if y == 3]
    if not threeOfAKind:
        return False, []
    else:
        return True, threeOfAKind

# Return the Poker cards
def getPoker(values):
    poker = [x for x, y in values if y == 4]
    if not poker:
        return False, []
    else:
        return True, poker

# Return the Straight cards
def getStraight(values):
    # Possibility of Ace being valued at 1
    if 14 in values:
        valuesLow = sorted([x if x != 14 else 1 for x in values], reverse=True)
        if isStraight(valuesLow):
            return True, valuesLow[0]

    if isStraight(values):
        return True, values[0]
    else:
        return False, []

# Function to determine is difference is all 1
def isStraight(values):
    difference = [abs(j-i) for i,j in zip(values[:-1], values[1:])]
    return all(x == 1 for x in difference)

# Return the Flush cards
def getFlush(values, suits):
    # Check that we have at least 5 cards
    if len(suits) != 5
        return False, []

    # Retrieve first suit and compare with the rest
    if all(suit == suits[0] for suit in suits):
        return True, values
    else:
        False, []


####################### CARDS FROM DECKS #####################################
# Function generates a 52 cards deck
def getCardsDeck():
    # Aces default value is 14, changed to 1 only when used in a straight
    values = list(range(2,15))
    suits = ['clubs','diamonds','hearts','spades']

    return [card for card in itertools.product(values,suits)]

# Function returns N cards from [decks] cards decks
def getCards(numOfCards):
    deck = getCardsDeck()

    if numOfCards > len(deck):
        numOfCards = len(deck)

    random.shuffle(deck)
    return deck[:numOfCards]
