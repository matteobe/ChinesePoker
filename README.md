# Chinese Poker

This programm aims to:

* recognize playing cards, 
* calculate the points of a chinese poker game.

In a later stage, we also want the program to be able to:

* register players, 
* create tournaments to store multiple games between the same users and
* provide statistics of the hands played and type of points won by the players.

## Rules of the Game
The game of chinese poker: 

* is played with a 52 french cards deck. 
* can be played by a maximum of 3 players. 

The goal of the game is to place the cards in a *pyramid* of hands:

* 3 cards at the top,
* 5 cards in the middle and
* 5 cards at the bottom.

*Hierarchy rule:* The hand at the bottom must be worth more than the hand in the middle, and the hand in the middle must be worth more than the hand at the top.

### How to Play
The game begins with each player being dealt 5 cards, which he can place wherever he wants in the *pyramid*.

After this initial phase we go around the table (clockwise or counter-clockwise) and each player in turn picks 3 cards from the deck and places 2 cards in the *pyramid* and discards the last card. After 4 rounds around the table, the game ends.

### Mis-Set
If the hands in the *pyramid* don't respect the hierarchy rule the player *mis-sets*, meaning that he doesn't make any points and gets *scooped* by his opponent.

### Fantasy Mode
A player that is able to place a combination in the top row worth more than a pair of Jacks reaches *Fantasy* mode.

When a player is in *Fantasy*-mode he receives 14 cards at the beginnig of the game and can prepare his *pyramid* with 13 of the 14 cards he received. One of the 14 cards must be discarded. 

The other players continue playing, as if the player in *Fantasy* mode was present. 

#### Special combinations
If a player in *Fantasy* mode is able to place a: 
 
* Poker in the bottom hand, 
* Three of a kind in the top hand, 

or combinations worth more, then he remains in *Fantasy* mode.


## Calculate points
The points are calculated by comparing two players *pyramids*. Each level of the *pyramid* is won by having the better hand. 

For each level of the *pyramid* won, the player gets 1 point. 

### Scoop
If a player wins all three levels of the *pyramid*, then he *scoops* his opponent and gets a 3 point bonus.

### Hands Points
The hands generate points as indicated in the following table:

| Hand      | Bottom | Middle | Top   |
| --------- |:------:|:------:|:------:|
| Pair | 0 | 0 | 1 (6), 2 (7),... |
| Three Of A Kind | 0 | 2 | 10 (2), 11 (3),... |
| Straight | 2 | 4 | - |
| Flush | 4 | 8 | - |
| Full House | 6 | 16 | - |
| Poker | 10 | 20 | - |
| Straight Flush | 15 | 30 | - |
| Royal Flush | 25 | 50 | - |
