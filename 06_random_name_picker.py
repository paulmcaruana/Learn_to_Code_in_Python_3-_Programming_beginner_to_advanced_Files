import random

people = []

while len(people) < 8:
    person = input("Type the name of a person: ")
    people.append(person)

print("The name chosen is: ", random.choice(people))
