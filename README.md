# NYT Spelling Bee Solver

This is a solver for the NYT Spelling Bee game.
When you run the program it asks you for the center tile letter and then the other letters one at a time.

# How to run
1. Clone this repository
2. Change/modify words.txt if you want to use a different word list
2. Run `chmod +x solver.py`
3. Run `./solver.py` and enter required input
	- Or run `./solver.py -f` to output to a text file with the date in the filename
4. Output is sorted with highest points first

# Wordlist
For my word list I used a custom wordlist generated from http://app.aspell.net/create using SCOWL with parameters:
  - diacritic: strip
  - max_size: 80
  - max_variant: 1
  - special: hacker
  - spelling: US

I used a large wordlist that will result in a lot of false positives, but these aren't penalized from my understanding of the game.
