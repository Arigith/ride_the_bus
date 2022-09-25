'''
Round 3. Inside or Outside?”
The player guesses whether the next card is **inside or outside**.

What should happen
1. System chooses random 2 random numbers
2. User choses if they think the next card will be inside or outside the 2 chosen numbers (ie if system chose 3 and 5 then inside would be 4 and outside would be any other number)
3. System chooses a third number
4. System checks if user was correct
5. If user was incorrect then system prints that the user looses and adds 1 to thier amount of drinks required to drink
6. If user was correct then print a win statement and print the total drinks to drink
'''

import random

drinks_count = 0

