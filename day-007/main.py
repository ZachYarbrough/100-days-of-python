import random

hangman_ascii = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_bank = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

hangman_step = 0
print("Welcome to Hangman! Can you guess the word before he hangs?")
print(hangman_ascii[hangman_step])

chosen_word = word_bank[random.randint(0, len(word_bank) - 1)]
word_display = []
word_length = len(chosen_word)

for _ in range(word_length):
    word_display.append("_")

print(' '.join(word_display))

end_of_game = False

while not end_of_game:
    user_input = input("Guess a letter:\n").lower()

    if user_input in word_display:
        print(f"You have already guessed the letter: {user_input}! Try Again.")
        continue

    if user_input not in chosen_word:
        hangman_step += 1

    for position in range(word_length):
        if user_input == chosen_word[position]:
            word_display[position] = user_input
            
    print(hangman_ascii[hangman_step])
    print(' '.join(word_display))
    
    if "_" not in word_display:
        print("You won!")
        end_of_game = True
    elif hangman_step == 6:
        print(f"You lose! The word was: {chosen_word}")
        end_of_game = True
        


