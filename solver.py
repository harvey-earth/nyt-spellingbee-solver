#!/usr/bin/env python

import sys

center = ''                 # string value for center
letters = set()             # set of tile letters
panagrams_to_try = set()    # set of panagrams to try
words_to_try = set()        # set of words to try in the game
best_words = dict()         # dictionary of words and point value

# Get center tile
while True:
    center_input = input("Please enter the center tile letter:").lower()
    # Check for correct input
    if center_input.isalpha() and (len(center_input) == 1):
        # Add letter to center and letters set then break out of this loop
        center = center_input
        letters.add(center_input)
        break
    # Error checks failed, message user and try again
    print("Please enter a single character\n")
    
# There are 7 tiles in total
while len(letters) < 7:
    c = input("Please enter the next tile letter:").lower()
    if c.isalpha() and (len(c) == 1):
        letters.add(c)
    
# Open wordfile and read into all_words list
# Change/replace this file to use a different word list
try:
    wordfile = open('words.txt', 'r')
    all_words = wordfile.readlines()
finally:
    wordfile.close()

for word in all_words:
    # Normalize
    word = word.strip().lower().replace("'","")
    # Check if the word meets all conditions while failing fast
    if (len(word) >= 4) and (center in word) and (set(word).issubset(letters)):
        # Check if panagram
        if letters.issubset(set(word)):
            panagrams_to_try.add(word)
        else:
            words_to_try.add(word)

# Add panagrams and words with points to dictionary
for word in panagrams_to_try:
    points = len(word) + 7
    best_words[word] = points

for word in words_to_try:
    points = len(word)
    best_words[word] = points
        
print("Possible words are:")
# Sort words with longest printed first, as these are worth the most points
for word in sorted(best_words.items(), key = lambda item: item[1], reverse = True):
    printed_word = word[0].upper()
    print(printed_word + "\tpoints: " + str(word[1]))
