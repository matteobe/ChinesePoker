# Function displays the hand of a player

import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

####################### MODULE VARIABLES ###################################
this = sys.modules[__name__]
this.parDir = os.path.abspath(os.pardir)
this.imgPath = os.path.join(this.parDir,"img/cards/")
this.fig = plt.figure()

# Function displays the hands of a player
def displayHands(cards):
    position = 1
    for card in cards:
        plotCard(card, position)
        position = position + 1

    # Remove spaces between subplots
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()


# Function plots card in the correct subplot space
def plotCard(card, position):
    # Adjust position indexing
    if position < 6:
        position = position + 10
    elif position > 10:
        position = position - 10
    # Add a subplot
    ax = this.fig.add_subplot(3,5,position)
    # Get image name
    imgName = "%i_%s.png" % (card[0], card[1])
    img = mpimg.imread(this.imgPath + imgName)
    imgplot = plt.imshow(img)
    # Clear axes
    plt.axis('off')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
