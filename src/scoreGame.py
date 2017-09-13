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
from collections import Counter

# Possible hands
hands = ['High Card', 'Pair', 'Two Pairs', 'Three Of A Kind','Straight',
         'Flush', 'Full House', 'Poker', 'Straight Flush', 'Royal Flush']


# Get points for 2 or 3 players
def getPoints(player1Cards, player2Cards, player3Cards=None):
    # Case with 2 players
    if player3Cards is None:
        return getPoints2Players(player1Cards, player2Cards)
    # Case with 3 players
    g12 = getPoints2Players(player1Cards, player2Cards)
    g13 = getPoints2Players(player1Cards, player3Cards)
    g23 = getPoints2Players(player2Cards, player3Cards)
    return [g12[0]+g13[0], g12[1]+g23[0], g13[1]+g23[1]]


def getPoints2Players(player1Cards, player2Cards):
    # Get the played hands for both players
    p1Hands = getPlayedHands(player1Cards)
    p2Hands = getPlayedHands(player2Cards)

    # Check if the hands are valid
    p1ValidHands = areValidHands(p1Hands)
    p2ValidHands = areValidHands(p2Hands)

    # Check higher hand for each layer
    bottomHigher = higherHand(p1Hands[0],p2Hands[0])
    middleHigher = higherHand(p1Hands[1],p2Hands[1])
    topHigher = higherHand(p1Hands[2],p2Hands[2])
    winnerHand = [bottomHigher, middleHigher, topHigher]

    # If both players mis-set, they both get 0 points
    if not p1ValidHands and not p2ValidHands:
        return [0,0]

    # When both players have valid hands
    if p1ValidHands and p2ValidHands:
        layerPoints = sum([1 if x else -1 for x in winnerHand])
        # Scoop case
        if layerPoints == 3:
            layerPoints = layerPoints + 3
    # Mis-set cases
    elif p1ValidHands and not p2ValidHands:
        layerPoints = 6
    else:
        layerPoints = -6

    # Count the hands points for both players
    if p1ValidHands:
        p1HandsPoints = getHandsPoints(p1Hands)
    else:
        p1HandsPoints = 0
    if p2ValidHands:
        p2HandsPoints = getHandsPoints(p2Hands)
    else:
        p2HandsPoints = 0

    # Calculate the total points
    totalPoints = layerPoints + p1HandsPoints - p2HandsPoints
    # Return the results
    return [totalPoints, -totalPoints]


# Compute the points from the hands played
def getHandsPoints(hands):
    # Points system
    bottomPointsLookup = [0, 0, 0, 0, 2, 4,  6, 10, 15, 25]
    middlePointsLookup = [0, 0, 0, 2, 4, 8, 16, 20, 30, 50]

    bottomPoints = bottomPointsLookup[hands[0][0]]
    middlePoints = middlePointsLookup[hands[1][0]]
    # Top hand is a Pair
    if hands[2][0] == 1:
        topPoints = max(0, hands[2][1][0] - 5)      # 66 gives 1 point
    # Top hand is a Three of a Kind
    elif hands[2][0] ==3:
        topPoints = hands[2][1][0] + 8              # 222 gives 10 points
    else:
        topPoints = 0
    return bottomPoints + middlePoints + topPoints


# Check if the hands played are valid
def areValidHands(hands):
    # Check that bottom hand is higher1 than middle hand
    bottomHigher = higherHand(hands[0],hands[1])
    middleHigher = higherHand(hands[1],hands[2])

    if bottomHigher and middleHigher:
        return True
    return False


# Check if the first hand is larger than the second
def higherHand(firstHand, secondHand):
    # Check if the first hand is higher more than the second hand
    if firstHand[0] > secondHand[0]:
        return True
    elif firstHand[0] == secondHand[0]:
        difference = [i-j for i,j in zip(firstHand[1], secondHand[1]) if i-j != 0]
        if difference and difference[0] > 0:
            return True
    return False


# Function returns the 3 hands played in the 3 layers
def getPlayedHands(cards):
    # Break the hand in the individual hands
    bottomCards = sorted(cards[:5], key=lambda card: card[0], reverse=True)
    middleCards = sorted(cards[5:10], key=lambda card: card[0], reverse=True)
    topCards = sorted(cards[10:], key=lambda card: card[0], reverse=True)

    # Score the three hands
    bottomHand = getHand(bottomCards)
    middleHand = getHand(middleCards)
    topHand = getHand(topCards)

    return [bottomHand, middleHand, topHand]


def getHand(cards):
    # Retrieve array of values and array of suits
    values = [card[0] for card in cards]
    suits = [card[1] for card in cards]
    valuesFrequency = Counter(values).most_common()     # Cards frequency

    # First check if we have a pair (Pair, Two Pairs, Full House)
    bPair, valPair = getPairs(valuesFrequency)
    bThree, valThree = getThreeOfAKind(valuesFrequency)
    bPoker, valPoker = getPoker(valuesFrequency)
    bStraight, valStraight = getStraight(values)
    bFlush, valFlush = getFlush(values, suits)

    # Use an ID to identify the hands:
    #   High Card (0), Pair (1), Two Pairs (2), Three of a Kind (3),
    #   Straight (4), Flush (5), Full House (6), Poker (7),
    #   Straight Flush (8), Royal Flush (9)
    #
    # High Card (0)
    if not bPair and not bThree and not bPoker and not bStraight and not bFlush:
        return [0, values]
    # Pair (1), Two Pairs (2)
    if bPair and not bThree:
        # Retrieve the high cards
        highCards = [x for x in values if x not in valPair]
        if len(valPair) == 1:
            valPair.extend(highCards)
            return [1, valPair]
        else:
            valPair.extend(highCards)
            return [2, valPair]
    # Three of a Kind (3)
    if bThree and not bPair:
        highCards = [x for x in values if x not in valThree]
        valThree.extend(highCards)
        return [3, valThree]
    # Straight (4)
    if bStraight and not bFlush:
        return [4, valStraight]
    # Flush (5)
    if bFlush and not bStraight:
        return [5, values]
    # Full House (6)
    if bPair and bThree:
        valFull = [valPair, valThree]
        return [6, valFull]
    # Poker (7)
    if bPoker:
        return [7, valPoker]
    # Straight Flush (8)
    if bStraight and bFlush and valStraight != 14:
        return [8, valStraight]
    # Royal Flush (9)
    return [9, 14]


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
    if len(suits) != 5:
        return False, []

    # Retrieve first suit and compare with the rest
    if all(suit == suits[0] for suit in suits):
        return True, values
    else:
        return False, []


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
