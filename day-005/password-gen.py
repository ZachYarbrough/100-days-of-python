import random

print("Welcome to the PyPassword Generator!")

letter_count = int(input("How many letters would you like in your password?\n"))

symbol_count = int(input("How many symbols would you like in your password?\n"))

number_count = int(input("How many numbers would you like in your password?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


password = []

for number in range(1, letter_count + 1):
    password.append(letters[random.randint(1, len(letters) - 1)])

for number in range(1, symbol_count + 1):
    password.append(symbols[random.randint(1, len(symbols) - 1)])

for number in range(1, number_count + 1):
    print(number)
    password.append(symbols[random.randint(1, len(numbers) - 1)])

random.shuffle(password)

print(f"Here is your password: {''.join(password)}")