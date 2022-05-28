# Randomisation Module
import random
# Easily import your own modules
import my_module

# Returns a random integer
random_integer = random.randint(1, 10)
#Returns random float between 0 and 1
random_float = random.random()

# print(random_integer)
# print(random_float)
# print(my_module.pi)

# Data Structure - Lists

states = ["Texas", "Florida", "Maine", "California"]
states.append("New York")
states.extend(["Rhode Island", "Washington"])
# -1 index will print the last element of the list.
print(states)