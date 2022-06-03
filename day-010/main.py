def my_function(a, b):
    result = a * b
    return result

print(my_function(3, 2))
# '.title()' uppercases the first letter of every word and lowercases the rest
def format_name(first_name, last_name):
    return f"{first_name.title()} {last_name.title()}"

# You can add 'input()' methods as parameters of a function

print(format_name(input("What is your first name? "), input("What is your last name? ")))

# Docstrings
# A small bit of documentation that allows you to get a description of your method when hovering over
# Use """ """ to write one.

def docstring_func(string):
    """Returns a string when called"""
    return string

docstring_func("Docsign Example")