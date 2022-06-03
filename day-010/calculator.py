print("Welcome to the Python Calculator")

def calculation(num_1):
    """Calculates numbers based on user input"""
    print("'+' '-' '*' '/'")
    operation = input("Pick an operation: ")

    num_2 = float(input("What's the second number: "))
    output = 0
    if operation == '+':
        output = num_1 + num_2
        print(f"{num_1} + {num_2} = {output}")
    elif operation == '-':
        output = num_1 - num_2
        print(f"{num_1} - {num_2} = {output}")
    elif operation == '*':
        output = num_1 * num_2
        print(f"{num_1} * {num_2} = {output}")
    elif operation == '/':
        output = num_1 / num_2
        print(f"{num_1} / {num_2} = {output}")
    else:
        'invalid operation'
    cont_calc = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
    if cont_calc == 'y':
        calculation(output)
    elif cont_calc == 'n':
        calculation(float(input("What's the first number: ")))

print(calculation(float(input("What's the first number: "))))