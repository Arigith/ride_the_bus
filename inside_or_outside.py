'''
Round 3. Inside or Outside?”
The player guesses whether the next card is **inside or outside**.

What should happen
1.  System chooses random 2 random numbers
2.  User choses if they think the next card will be inside or outside the 2 chosen numbers (ie if system chose 3 and 5
    then inside would be 4 and outside would be any other number)
3.  System chooses a third number from a list that excludes the 2 original chosen numbers
4.  System checks if user was correct
5.  If user was incorrect then system prints that the user looses and adds 1 to thier amount of drinks required to drink
6.  If user was correct then print a win statement and print the total drinks to drink
'''

import random

ioround = True

drinks_count = 0

deck_range = range(1, 14)
deck_size = 2
deck = sorted(random.sample(deck_range, deck_size))

while ioround == True:
    for hole_card_1, hole_card_2,in zip(deck[:-1],deck[1:]):
        # print(hole_card_1)
        # print(hole_card_2)
        next_card = random.choice([dr2 for dr2 in deck_range if dr2 != hole_card_1 and dr2 != hole_card_2])
        # print(next_card)
        user_guess = input(f'The dealer has picked {hole_card_1} and {hole_card_2}.\nWill the next card be inbetween or outside?(i/o)\n').lower()
        if user_guess != 'i' and user_guess != 'o':
            print(f'{user_guess} is not a valid choice. Please try again')
        correct_option = 'i' if next_card > hole_card_1 and next_card < hole_card_2 else 'o'
        if user_guess != correct_option:
            print(f'Sorry you loose as the next card was {next_card}.')
            drinks_count += 1
        else:
            print(f'The next card was {next_card}. You win')
            print(f'Your drink tally is {drinks_count}')
            ioround = False