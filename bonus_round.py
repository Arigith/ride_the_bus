'''
4. “Bonus round”
The player guesses whether the card is **Diamonds, Hearts, Spades or Clubs**.

What should happen
1. System chooses random suit
2. User choses what suit they think the system chose
3. system checks if user was correct
4. system prints if user was correct or incorrect
'''

import random
drink_count = 0
suit_choices = ('Diamonds', 'Hearts', 'Spades', 'Clubs')

is_guess_right = False

while is_guess_right != True:
    dealers_choice = random.choice(suit_choices)
    player_choice = input('What colour did the dealer choose?\nChoices are Diamonds, Hearts, Spades or Clubs\n').capitalize()
    if player_choice != 'Diamonds' and player_choice != 'Hearts' and player_choice != 'Spades' and player_choice != 'Clubs':
        print(f'\n{player_choice} is an invalid choice please try again.\n')
    elif player_choice == dealers_choice:
        print(f'Your guess of {player_choice} was correct. \n YOU WIN!')
        print(f'The total drinks tally is {drink_count}')
        is_guess_right = True
    else:
        print(f'You guessed {player_choice} while the dealer chose {dealers_choice}.\n YOU LOSE! ')
        drink_count += 1