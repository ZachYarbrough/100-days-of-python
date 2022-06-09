# OOP

class Turtle:
    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

turtle = Turtle("Ben", 1, 1)

print(turtle.name)

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)