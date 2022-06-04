import random
from tracemalloc import start

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

score = 0
dealers_score = 0

starting_cards = [random.choice(cards), random.choice(cards)]
score += starting_cards[0] + starting_cards[1]

dealers_starting_cards = [random.choice(cards), random.choice(cards)]
dealers_score += dealers_starting_cards[0] + dealers_starting_cards[1]

def deal_card(input_value):
    global score
    if input_value == 'y':
        new_card = random.choice(cards)
        starting_cards.append(new_card)

        print(f"You drew a {new_card}")
        score += new_card
        if score > 21:            
            print(f"Your final hand is {starting_cards} which sums up to {score}")
            print("You went over 21! You lose!")
            return
        else:
            deal_card(input("Type 'y' to get another card, type 'n' to pass: "))
    elif input_value == 'n':
            print(f"Your final hand is {starting_cards} which sums up to {score}")
            print(f"The dealer's final hand is {dealers_starting_cards} which sums up to {dealers_score}")

            if score > dealers_score:
                print("You win!")
            elif score == dealers_score:
                print("You tied with the house!")
            else:
                print(f"You lose! The dealer had {dealers_score}")
            return

print(f"Your cards are {starting_cards} which sum up to {score}")

if dealers_score == 21 and len(dealers_score) == 2:
    print("The dealer drew a blackjack! You lose!")
    exit()

print(f"The dealer's first card is {dealers_starting_cards[1]}")
deal_card(input("Do you wish to draw another card? Type 'y' to get another card, type 'n' to pass: "))