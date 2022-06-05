import random

attempts = 0
game_over = False

def game():
    global game_over 
    game_over = False
    random_number = random.randint(1, 101)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    def choose_difficulty():
        global attempts

        difficulty =  input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


        if difficulty == 'easy':
            attempts = 10
        elif difficulty == 'hard':
            attempts = 5
        else:
            print("Please input a valid answer.")
            choose_difficulty()

    def guess_number():
        global attempts
        global game_over

        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            game_over = True
            return print("You guessed the number! You win!")
            
        elif guess > random_number:
            print("Your guess was too high!")
        elif guess < random_number:
            print("Your guess was too low")
        attempts -= 1

    choose_difficulty()
    while attempts > 0 and not game_over:
        guess_number()

    if attempts == 0:
        new_game = input("You ran out of attempts! Would you like to play again? Type 'y' or 'n': ")
    else: 
        new_game = input("Would you like to play again? Type 'y' or 'n': ")

    if new_game == 'y':
        game()
    else:
        print("Thanks for playing!")
game()