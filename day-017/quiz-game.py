class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

score = 0
questions = [
    Question("Does a snail bleed green blood? (T/F) ", True),
    Question("Is the grass blue? (T/F) ", False),
    Question("Is the sky blue? (T/F) ", True),
    Question("Does 2 * 8 = 16? (T/F) ", True)
]

for index in range(0, len(questions)):
    current_input = input(questions[index].text).lower()
    
    if current_input == 't':
        current_bool = True
    else:
        current_bool = False

    if current_bool == questions[index].answer:
        score += 1
        print("You got the answer correct!")
        print(f"Your score is {score} out of {index + 1}")
    else:
        print(f"You got it wrong! The correct answer was: {questions[index].answer}")
        print(f"Your score is {score} out of {index + 1}")
    

print(f"You got {score} out of {len(questions)} correct! Thanks for playing!")