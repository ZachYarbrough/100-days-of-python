# Creating Custom Classes

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)


user_1 = User('Zach', 22)

user_1.get_name()