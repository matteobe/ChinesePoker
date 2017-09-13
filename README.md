# ChinesePoker

The programm aims to:

* calculate the points of a game
* recognize playing cards
* provide statistics of the hands played and points won

## Chinese poker
The game of chinese poker: 

* is played with a 52 french cards deck. 
* can be played by a maximum of 3 players. 

The goal of the game is to place the cards in a pyramid of:

* 5 cards at the base,
* 5 cards in the middle and
* 3 cards at the top.

The hand at the bottom must be worth more than the hand in the middle, and the hand in the middle must be worth more than the hand at the top.
If the hands don't respect the rule mentioned above, the player "mis-sets".

The game begins with each player having 5 cards which he can place wherever he wants in the "pyramid".


After this initial phase we go around the table (clockwise, counter-clockwise) and each player picks 3 cards from the deck and places 2 cards in the "pyramid" and one card is discarded.
After 4 rounds around the table, the game ends.

### Fantasy
A player that is able to place a combination in the top row worth more than a pair of Jacks reaches "Fantasy"-mode

When a player is in "Fantasy"-mode he receives 14 cards at the beginnig of the game and can prepare his "pyramid". One of the 14 cards must be discarded. 

The other players continue playing, as if the player in "Fantasy"-mode is present. 

#### Special combinations
If a player is able to place a: 
 
* Poker in the bottom hand
* Three of a kind in the top hand

or combinations worth more, the player remains in "Fantasy"-mode.


## Calculate points
The points are calculated by comparing two players "pyramid". Each level of the pyramid is won by having the better hand. 

For each level of the "pyramid" won, the player gets 1 point. Additionally, if a player wins all three levels he *scoops* his opponent and gets a 3 point bonus.

Furthermore, the hands generate points as indicated in the following table:

| Hand      | Bottom | Middle | Top   |
| --------- |:------:|:------:|:------:|
| Pair | 0 | 0 | 1 (66) |
| Tris | 0 | 2 | 10 (222) |
| Straight | 2 | 4 | - |
| Flush | 4 | 8 | - |
| Full House | 6 | 16 | - |
| Poker | 10 | 20 | - |
| Straight Flush | 15 | 30 | - |
| Royal Flush | 25 | 50 | - |



