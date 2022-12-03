#---------------------------------------------------------------------#
# File: /home/adamo/Adam/Coding/python-unscramble/unscramblers/dict-unscramble.py
# Project: /home/adamo/Adam/Coding/python-unscramble/unscramblers
# Created Date: Saturday, December 3rd 2022, 8:35:01 pm
# Description: 
# Author: Adam O'Neill
# Copyright (c) 2022 Adam O'Neill
# -----
# Last Modified: Sat Dec 03 2022
# Modified By: Adam O'Neill
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
# 2022-12-03	AO	NEXT: scramble up the words into every combinantion and set this as the key to the original unscrambled word
# 2022-12-03	AO	Sucessfully imports words and decided which dict to put them into
#---------------------------------------------------------------------#

# This method of unscrambling data will use dictionaires and lookup what the word should be


# Import every english word
from english_words import english_words_lower_set


def calculateScrambledWords(word):
    #sword - scrambled word    
    for x in range(len(word)):
        # scramble up word
        # Add to list 


def addWordToQuar(dictionary,word,sword):
    #sword - scrambled word
    pass


def calculateArrangement(word):
    length = len(word)
    arrangementNum = factorial(length)

def factorial(number):
    if number == 1:
        return 1
    else:
        return (number* factorial(number-1))


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
     

    elif word[0] < "M":
        # Second quater
    
    elif word[0] < "S":
        # Last quater
    else:
        # Final quater  
    
print(quar1)
