#---------------------------------------------------------------------#
# File: /home/adamo/Adam/Coding/python-unscramble/unscramblers/dict-unscramble.py
# Project: /home/adamo/Adam/Coding/python-unscramble/unscramblers
# Created Date: Saturday, December 3rd 2022, 8:35:01 pm
# Description: 
# Author: Adam O'Neill
# Copyright (c) 2022 Adam O'Neill
# -----
# Last Modified: Wed Dec 14 2022
# Modified By: Adam O'Neill
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
# 2022-12-14	AO	Succesfully scrambles words and bring in every word but so many things, it breaks computer
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
    res=set()
    def backtrack(word, index, length): 
        if index==length: 
            res.add(''.join(word))
        else: 
            for j in range(index,length): 
                word[index], word[j] = word[j], word[index] 
                backtrack(word, index+1, length) 
                word[index], word[j] = word[j], word[index]  
    
    word_in_list = list(word) 
    backtrack(word_in_list, 0, len(word))
    return res

def main():
    # Create 4 dictionaries splitting up all the words into alphabetical quaters
    dictonary = {}


    for word in english_words_lower_set:
        word = word.lower()
        dictonary[word] = calculateScrambledWords(word)
    
    print(dictonary)

main()