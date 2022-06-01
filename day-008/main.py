# Parameters

def greet(name, location):
    print(f"Hello {name} from {location}!")

#Positional arguments read the parameters from left to right
greet("Jeremy", "Austin")

# Keyword arguments allow you to define the parameters in the wrong order
greet(location="Galveston", name="Zach")