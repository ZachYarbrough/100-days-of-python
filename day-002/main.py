# Data Types

# String
string = "Hello"

print(string[0])
print(len(string))

# Integers
# You can use '_' as a comma when writing code, python will ignore any '_' in the output
print(123_456_789 + 123_456_789)

# Float
print(3.14159)

# Boolean
# True and False must be capitalzed in order to work
boolean = True
print(type(boolean))

# When you divide it will return a float even if it is an even division like 6 / 3
# 'x ** y' is x to the power of y

# 'round()' allows you to round a float variable
# You can also use the second parameter to specify how many decimal places to round to
# Rounds to a whole number, output is 6
print(round(2 + 3.59))
# Rounds to the first decimal place, output is 5.6
print(round(2 + 3.59, 1))

# f-String
# Similar to a template literal in JavaScript
score = 1
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")