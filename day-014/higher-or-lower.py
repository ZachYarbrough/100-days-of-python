from unicodedata import name
from game_data import data
import random

score = 0

def game():
    global score
    is_playing = True
    while is_playing:
        first_int = random.randint(0, len(data) - 1)
        second_int = random.randint(0, len(data) - 1)

        if first_int == second_int:
            second_int -= 1

        first_choice = data[first_int]
        second_choice = data[second_int]
        user_input = input(f"Who has more followers? Type 'a' for {first_choice.get('name')} or 'b' for {second_choice.get('name')}: ").lower()
        if first_choice.get('follower_count') > second_choice.get('follower_count') and user_input == 'a':
            print(f"You got it right! {first_choice.get('name')} has more followers than {second_choice.get('name')}!")
            score += 1
            print(f"Your current score: {score}")
        elif first_choice.get('follower_count') < second_choice.get('follower_count') and user_input == 'b':
            print(f"You got it right! {second_choice.get('name')} has more followers than {first_choice.get('name')}!")
            score += 1
            print(f"Your current score: {score}")
        else:
            print(f"You guessed wrong! Your final score: {score}.")
            is_playing = False

game()