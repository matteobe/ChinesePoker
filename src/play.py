# This file is the entry point for the game
#
#

import scoreGame as scr


if __name__ == '__main__':
    # Get the two players hands
    player2 = scr.getCards(13)

    # Create a vector of cards
    player1 = [(14,'spades'),(2,'spades'),(5,'spades'),(7,'spades'),(10,'spades'),
               (10,'clubs'),(10,'spades'),(6,'diamonds'),(6,'diamonds'),(5,'clubs'),
               (4,'spades'),(4,'hearts'),(2,'clubs')]
    player2 = [(11,'hearts'),(10,'hearts'),(2,'hearts'),(3,'hearts'),(4,'hearts'),
               (13,'clubs'),(13,'spades'),(7,'clubs'),(7,'hearts'),(4,'clubs'),
               (4,'hearts'),(4,'clubs'),(7,'spades')]
               
    # Call the combination Function
    points = scr.getPoints(player1, player2, player1)
    print(points)
