letter_bank = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

def inputs():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("Invalid Input. Try again")
        inputs()

def encrypt(word, shift):
    encrypted_text = ''
    for char in word:
        encrypted_text += letter_bank[letter_bank.index(char) + shift]
    print(encrypted_text)
    inputs()

def decrypt(word, shift):
    decrypted_text = ''
    for char in word:
        decrypted_text += letter_bank[letter_bank.index(char) - shift]
    print(decrypted_text)
    inputs()

inputs()