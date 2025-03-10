# HIGHER OR LOWER PART OF GAME
# WHAT SHOULD HAPPEN
# 2 System chooses random card as the hole card
# 3 Player chooses if next card will be higher or lower then chosen card
# 4 System chooses another random card and checks if this was higher or lower then the hole card
# 6 System then checks if user was correct
# 7a If player is correct then let them know they won
# 7b If player is incorrect then let them know they have lost

import random

drink_total = 0
deck_size = 2
# Request system to generate 2 random numbers between 1 and 13
# to stop any repeats I added None to indicate end of deck
deck = random.sample(range(1, 14), deck_size) + [None]

while True:
# Splits the 2 chosen numbers into chosen card (hole_card and next_card)
    for hole_card, next_card in zip(deck[:-1],deck[1:]):
        print(hole_card)
        print(next_card)
# Arguement to say that if the next card is greater then hole card then this is higher otherwise it is lower
        correct_guess = 'h' if next_card > hole_card else 'l'
# Player chooses higher or lower
        guess = input(f'current card is {hole_card} is the next higher or lower? ') 
# System checks if player was correct or incorrect
# If play was incorret then print following statement
        if guess != correct_guess:
            print(f'You loose the next card was {next_card}')
            drink_total += 1
        else:
# If player was correct then print winner
            print(f'you choice of {guess} was correct. You win')
            print(f'Your drink tally is {drink_total}')
            hlround = False