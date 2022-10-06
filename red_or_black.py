'''
1. “Red or black?”
The player guesses whether the card is **red or black**.

What should happen
1. System chooses random colour from Red or Black
2. User choses what colour they think the system chose
3. System checks if user was correct
4. If incorrect then system prints message stating they are wrong and adds a drink to the required drinks tally
5. If correct then system prints message stating they won and then tells total of drinks required
'''
import random

drink_count = 0

colour_choices = ('Red', 'Black')

is_guess_right = False

while is_guess_right != True:
    dealers_choice = random.choice(colour_choices)
    player_choice = input('What colour did the dealer choose? Red or Black\n').capitalize()
    if player_choice != 'Red' and player_choice != 'Black':
        print(f'\n{player_choice} is an invalid choice please try again.\n')
    elif player_choice == dealers_choice:
        print(f'Your guess of {player_choice} was correct. \n YOU WIN!')
        print(f'Your drink total is {drink_count}')
        is_guess_right = True
    else:
        print(f'You guessed {player_choice} while the dealer chose {dealers_choice}.\n YOU LOSE! ')
        drink_count += 1