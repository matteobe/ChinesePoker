"""
Cards recognition software for game of Chinese Poker

The game is played by creating a stack of 5,5,3 cards.
Each hand must be worth less than the hand below it.

The application also compares two players together and calculates the points
"""

import sys
import numpy as np
import cv2 as cv
import scoreGame as scr

####################### MODULE VARIABLES ###################################
# Retrieve this module
this = sys.modules[__name__]

# Store module variables
this.path = "/Users/matteo/Desktop/ChinesePoker/"


####################### COMPUTER VISION ##################################
# Function identifies cards by comparing with templates
# Suffers from scaling problems !!!
def getCards_Template(img):
    # Read in the template image
    template = cv.imread(this.path + "test/template_spades.jpeg",0)
    scale = 0.4
    template = cv.resize(template,None,fx=scale,fy=scale,interpolation=cv.INTER_AREA)
    w, h = template.shape[::-1]

    # Perform template matching
    res = cv.matchTemplate(img,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    # Show image
    showImage(img)

# Function returns an array containing the card values and their "color"
def getCards_Threshold(img):
    # Convert to gray image and blur
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(1,1),1000)

    # Threshold the image to search for contours
    # Use simple thresholding
    #flag, thresh = cv.threshold(blur, 200, 255, cv.THRESH_BINARY)
    #flag, thresh = cv.threshold(blur, 200, 255, cv.THRESH_BINARY)
    # Use adaptive gaussian thresholding
    thresh = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 121, 0)

    # Find the contours, sort them by area and keep the largest 3
    imgC, contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv.contourArea, reverse=True)[:3]

    # Iterate through the contours and separate the cards
    # Draw the contours on the image
    imgCD = cv.drawContours(img,contours,-1,(0,255,0),2)
    showImage(imgCD)

# Show image and wait for key stroke to destroy window
def showImage(img):
    cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    # Specify filename, load image and show it
    filename = this.path + "test/test_3.jpeg"
    #simgOrig = cv.imread(filename,0)

    # Scale image
    scale = 0.2
    #img = cv.resize(imgOrig,None,fx=scale,fy=scale,interpolation=cv.INTER_AREA)
