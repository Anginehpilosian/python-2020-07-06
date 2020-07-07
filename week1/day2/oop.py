# What is OOP? Object Oriented Programming
# What is an object?
# Why use an object?
# Why use OOP?

# DRY - Don't Repeat Yourself

# Person
# sid_name = 'Sidney'
# sid_location = 'California'

sidney = {
    # "key": "value"
    "first_name": "Sidney",
    "location": "California"
}
# print(sidney['first_name'])
# print(sidney['location'])

# tural_name = 'Tural'
# tural_location = 'New York'

tural = {
    # "key": "value"
    "first_name": "Tural",
    "location": "New York"
}

# chris_name = 'Chris'
# chris_location = 'SF'

chris = {
    # "key": "value"
    "first_name": "Chris",
    "location": "SF"
}

# Class


class Person:
    def __init__(self, f_name, location):
        # pass
        print('Creating a person!')
        self.first_name = f_name
        self.location = location
        # self.hobby = Hobby()
        self.hobby = []

        # print(self.first_name + ' created!')
        # print(f"{self.first_name} created!")

    def say_my_name(self):
        print(f"My name is {self.first_name}!")


beth = Person('Beth', 'Idaho')
ben = Person('Ben', 'Seattle')
tim = Person('Tim', 'LA')

# print(beth.say_my_name)
beth.say_my_name()
ben.say_my_name()
tim.say_my_name()

# Hobby
class Hobby:
    def __init__(self, name, costs, years=0, equipment=[]):
        print('Creating a person!')
        self.name = name
        self.years = years
        self.costs = costs
        self.equipment = equipment


pets = Hobby('Pets', 200, 1, ['harness', 'leash', 'dog'])
# print(pets.name)
# print(pets.equipment)

# sleep = Hobby('Sleep', 22, 2000, ['bed', 'blinds', 'sleeping mask', 'pillow'])
sleep = Hobby('Sleep', 2000)
# print(sleep.equipment)

matthew = Person('Matthew', 'Mars')
print(matthew.hobby)
# matthew.hobby.append(Hobby())
matthew.hobby.append(sleep)
print(matthew.hobby)
