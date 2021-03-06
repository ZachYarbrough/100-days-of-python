# 100 Days of Python

I purchased Dr. Angela Yen's 100 Days of Python class and am documenting what I learned and the errors that I come across in order to see my progress and create an archive of information relating to python.

Each directory will be labeled day-001, day-002, day-003 and will have my scratch .py file along with whatever the challenge that day was.

## Daily Takeaways

<details>
<summary>Day 1 - Console input and Variables</summary>

### What I learned
- I learned about printing and interacting with the console via `print()` and `input()`.
    ```py
    # Prints 'Hello World' into the terminal
    print("Hello World")

    # Prompts the user with an input asking what their name is
    input("What is your name?")
    ```
- I learned how to instantiate variables
    ```py
    # Stores the user input in the name variable
    name = input("What is your name?")

    # Prints the name that the user input
    print(name)
    ```
- I learned how to get the number of characters of a string using `len()` and that you can embed methods in other methods
    ```py
    # Returns the number of characters that the user input
    # If user inputs 'Zach' then length will return '4'
    length = len(input("What is your name?"))

    # Prints a string with using the length variable
    print("Your name is " + length + " characters long!")
    ```
### Takeaways
- Python3 is different than python. I ran into this error when using the input command:
    ```
    What is your name? Zach
    Traceback (most recent call last):
    File "day-001/main.py", line 2, in <module>
    name = input("What is your name?")
    File "<string>", line 1, in <module>
    NameError: name 'Zach' is not defined
    ``` 
    After further researching the error I realized that it was because I was using the wrong version of python and python v2 needed `raw_input()` rather than just `input()`. For future refrence make sure you run scripts using `$ python3 main.py` rather than just `$python main.py`

</details>

<details>
<summary>Day 2 - Data Types and String Manipulation</summary>

### What I learned
- I learned about the different Data Types in python
    - They are vary similar to C# variables with a few exceptions
    - Strings, Integers, Floats, and Booleans
- I learned how to type cast with `str(1234)` or `int("1234")` and type check with `type("Hello")`
- I learned about f-Strings which is very similar to a template literal but instead of using back ticks, you write it like this:
```py
variable = "variable"
print(f"This is a f-String with a {variable} inside")
```
- I learned how to round ints and floats using `round()`, you can specify how many decimals with the second parameter like so:
```py
# Will return 1235
round(1234.567)

# Will return 1235.57
round(1234.567, 2)
```
### Takeaways
- You can use `_` as commas in long numbers, python will ignore any `_` in the output 
```py
# Will output 246913578 with no `_`
print(123_456_789 + 123_456_789)
```

</details>

<details>
<summary>Day 3 - Control Flow and Logical Operators</summary>

### What I learned
- If statements work exactly the same as JS but with different syntax. They require a collon at the end of the if statement and rather than `{ }` for the content, you must indent all the code that is inside.
    ```py
    if 1 = 2:
        print('1 = 2')
    elif 1 = 1:
        print('1 = 1')
    else:
        print('1 != 1 or 2')
    ```
- Rather than `&&` `||` and `!` logical operators are written in english like so `and` `or` `not`
</details>

<details>
<summary>Day 4 - Randomisation and ython Lists</summary>

### What I learned
- You must import modules in python similar to importing files and packages in node. However, a lot of built in packages in node are not built in to python. For example, you must `import random` before you can use random methods
- Random has to take into account int or float, you can do this by either using `random.randint(x. y)` for an int between x and y or `random.random()` for a float between 0 and 1
- Lists in python work the exact same as arrays in JS

</details>

<details>
<summary>Day 5 - Loops</summary>

### What I learned
- Loops are written much more simply:
    ```py
    fruits = ['Apple', 'Orange', 'Banana']

    for fruit in fruits:
        print(fruit)
    ```
- You can use `range()` to mimic a javascript like for loop:
    ```py
    # Will print numbers until it reaches 100
    # range will not use the last digit in the second parameter (in this case 101, so the max is 100)
    # The 3 parameter is how the number will be incremeneted
    for number in range(1, 101, 1):
        print(number)
    ```

</details>

<details>
<summary>Day 6 - Functions</summary>

### What I learned
- Indentations are very important when using functions, 4 spaces (or 1 tab) is how you signify whether or not the content is inside a funciton or not
    ```py
    def my_function():
        print("This is in a function")
    ```

</details>

<details>
<summary>Day 7 - Hangman</summary>

### What I learned
- you can use `in` or `not in` to check if a string or character is in an array or string. I found this to be quite useful when creating the hangman project.
    ```py
    # Will return "string contains the word Test"
    string = "Test String"
    if "Test" not in string:
        print("string does not contain the word Test")
    else:
        print("string contains the word Test")
    ```

</details>

<details>
<summary>Day 8 - Parameters</summary>

### What I learned
- Parameters do not have to be in order based on definition:
    ```py
    # Positional Parameters by default and read from left to right
    # Will out put '1 2 3'
    def position_params(a, b, c):
        print(a, b, c)
    position_parans(1, 2, 3)

    # Keyword Parameters do not need to be in any order
    # Will out put '3 1 2'
    def position_params(a, b, c):
        print(a, b, c)
    position_parans(b=1, c=2, a=3)
    
    ```

</details>

<details>
<summary>Day 9 - Dictionaries and Nesting</summary>

### What I learned
- Dictionaries are basically just javascript objects:
    ```py
        capital_dict = {
            "France": "Paris",
            "Germany": "Berlin"
        }

        # You can add key value pairs like this
        capital_dict["Spain"] = "Madrid"
    ```
- If you pass a dictionary through a for loop it will only return the key:
    ```py
        capital_dict = {
            "France": "Paris",
            "Germany": "Berlin"
        }

        #This will print 'France' and 'Germany'
        for country in capital_dict:
            print(country)

        #This will print 'Paris' and 'Berlin'
        for capital in capital_dict:
            print(capital_dict[capital])
    ```

</details>

<details>
<summary>Day 10 - Functions with Outputs</summary>

### What I learned
- `.title()` formats a string no matter the input to have every first letter of a word be capitalized and the rest will be lowercased
    ```py
        # This will output 'Zach Yarbrough'
        def format_name(first_name, last_name):
            return f"{first_name.title()} {last_name.title()}"
        print(format_name("zACh", "YaRBRouGh"))

    ```
- You can write docstrings inside a function using 3 quotes like this: `"""This is a docstring"""` to write a breif description for your functions
    ```py
        def docstring_func(string):
        """Returns a string when called"""
        return string

        docstring_func("Docsign Example")
    ```

</details>

<details>
<summary>Day 11 - Blackjack Capstone Project</summary>

### Takeaways
- After 10 days of python, I am finding it really enjoyable. For this capstone project, we had to build the game of Blackjack and this required me to use pretty much everything I had learned previously, from functions to variables.
- I can not wait to get more in depth with python and its nuances. I find the language much more readable and easy to understand than javascript

</details>

<details>
<summary>Day 12 - Local and Global Scope</summary>

### What I learned
- You have to make a variable a global scope inside the function for you to use it
    ```py
    global_var = 1
    # Will return 2
    def global_function():
        global global_var
        return global_var += 1
    function()

    local_var = 1
    def local_function():
        local_var = 2
    # Will print out 2
    local_function()
    # Will print out 1
    print(local_var)
    ```
- You can make a constant by writing the variable name all uppercase:
    ```py
    CONSTANT_VARIABLE = 3
    print(CONSTANT_VARIABLE)
    ```

</details>

<details>
<summary>Day 13 - Debugging</summary>

### What I learned
- Today was learning about debugging, however I am already very familiar with debugging code while working with javascript. There were some cementing concepts that were good to go over, but in general I did not learn anythin new this lesson

</details>

<details>
<summary>Day 14 - Higher or Lower Game</summary>

### Takeaways
- I decided to use a while loop rather than recursion this time. I found that I had been using recursion to solve all the problems in the course work and the instructor kept using while loops instead. So I figured I would instead use a while loop to check if the user is still playing and it worked extremely well.

</details>

<details>
<summary>Day 15 - Coffee Machine</summary>

### Takeaways
- The coffee machine project was fairly simple. I am still really enjoying python and can not wait to get much mor in depth in later days.

</details>

<details>
<summary>Day 16 - Object Oriented Programming</summary>

### Takeaways
- We learned about OOP today. It is very straight forward after my experience with it in javascript. With a few differences:
- For example, instead of a constructor method where you define all of your attributes, python uses the __init__ method and you need to pass `self` inside the __init__ parameters as well.
    ```py
    class Student:
        def __init__(self, name, age)"
            self.name = name
            self.age = age
    
    student = Student("Zach", 22)
    # This will print out `Zach`
    print(student.name)
    ```

</details>

<details>
<summary>Day 17 - Creating Classes</summary>

### Takeaways
- I touched on creating classes yesterday and I think it is very simple. There is not much different when compared to JS.

</details>

<details>
<summary>Day 18 - Import Modules</summary>

### What I learned
- This lesson was getting me comfortable importing/installing python modules (packages in node)

</details>

<details>
<summary>Day 19 - Turtle Race</summary>

- I took a break from learning python so I could focus on data structures and algorithms for my amazon interview loop. However this was a fun lesson to get back in the rythmn.

### What I learned
- We learned more about the turtle package and it seems to be a fun package for creating simple games
- We touched on event listeners that watch for key inputs

</details>

<details>
<summary>Day 20 - Snake Game</summary>

### What I learned
- There is a time module you can use `import time` that will allow you to increment easily and do other things related to time

</details>

<details>
<summary>Day 21 - Snake Game Part 2</summary>

### What I learned
- It is difficult to import files across directories

</details>