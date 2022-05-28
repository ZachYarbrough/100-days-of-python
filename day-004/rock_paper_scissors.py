import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if choice == 0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''')
elif choice == 1:
    print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    ''')
elif choice == 2:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')

computer_choice = random.randint(0, 2)
print("Computer chose: ")

if computer_choice == 0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''')
elif computer_choice == 1:
    print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    ''')
elif computer_choice == 2:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')

if (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 0):
    print("You lose.\n")
elif (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1) or (choice == 0 and computer_choice == 2):
    print("You win!\n")
else:
    print("You tied.\n")