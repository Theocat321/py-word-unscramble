#---------------------------------------------------------------------#
# File: /home/adamo/Adam/Coding/python-unscramble/unscramblers/dict-unscramble.py
# Project: /home/adamo/Adam/Coding/python-unscramble/unscramblers
# Created Date: Saturday, December 3rd 2022, 8:35:01 pm
# Description: 
# Author: Adam O'Neill
# Copyright (c) 2022 Adam O'Neill
# -----
# Last Modified: Tue Dec 13 2022
# Modified By: Adam O'Neill
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
# 2022-12-13	AO	The bubble sort method doesnt work on longer words
# 2022-12-09	AO	Works for 3 letter words fully, attempted with 4 letter word, doesnt work
# 2022-12-09	AO	Succesfully finds the amount of combinations for amount of letters (3 combinations for a 3 letter word)
# 2022-12-03	AO	NEXT: scramble up the words into every combinantion and set this as the key to the original unscrambled word
# 2022-12-03	AO	Sucessfully imports words and decided which dict to put them into
#---------------------------------------------------------------------#

# This method of unscrambling data will use dictionaires and lookup what the word should be


# Import every english word
from english_words import english_words_lower_set


def calculateScrambledWords(word):
    # In the case of a "cat"
    # While there is not 6 items in array
    # iterate through cat wapping letters each time
    # cat, act, atc - now the loop for the first loop 
    # Loop from atc 3 more times to get cta
    # Think of it as passes in a bubble sort
    # tac, tca, cta
    wordCombinations = []
    wordCombinations.append(word)
    wordIterations = factorial(len(word))
    scrambled = False
    wordArr = createWordArray(word)
    for x in range(wordIterations): 
        for x in range(1,len(word)):
            temp = wordArr[x-1]
            wordArr[x-1] = wordArr[x]
            wordArr[x] = temp
            wordstr = createString(wordArr)
            if wordstr not in wordCombinations:
                wordCombinations.append(wordstr)
    return wordCombinations

        



def createWordArray(word):
    arr = []
    for letter in word:
        arr.append(letter)
    return arr

def createString(arr):
    string = ""
    for letter in arr:
        string = f"{string}{letter}"
    return string

def factorial(number):
    if number == 1:
        return 1
    else:
        return (number* factorial(number-1))

print(calculateScrambledWords("toby"))

def main():
    # Create 4 dictionaries splitting up all the words into alphabetical quaters
    quar1 = {}
    quar2 = {}
    quar3 = {}
    quar4 = {}


    for word in english_words_lower_set:
        word = word.lower()
        print(word[0])
        if word[0] < "g":
            # First quater
            pass
        elif word[0] < "M":
            # Second quater
            pass
        elif word[0] < "S":
            # Last quater
            pass
        else:
            # Final quater  
            pass
    print(quar1)
