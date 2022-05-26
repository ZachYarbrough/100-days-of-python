# 100 Days of Python

I purchased Dr. Angela Yen's 100 Days of Python class and am documenting what I learned and the errors that I come across in order to see my progress and create an archive of information relating to python.

Each directory will be labeled day-001, day-002, day-003 and will have my scratch .py file along with whatever the challenge that day was.

## Daily Blogs

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