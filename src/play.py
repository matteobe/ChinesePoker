# This file is the entry point for the game
#
#

import scoreGame as scr


if __name__ == '__main__':
    # Get the two players hands
    player2 = scr.getCards(13)

    # Create a vector of cards
    cards = [(10,'spades'),(11,'spades'),(12,'spades'),(9,'spades'),(14,'spades'),
             (10,'clubs'),(6,'spades'),(10,'diamonds'),(9,'diamonds'),(9,'clubs'),
             (5,'spades'),(5,'hearts'),(14,'clubs')]

    # Call the combination Function
    bottomHand, middleHand, topHand = scr.getPlayedHands(cards)

    print(middleHand)
