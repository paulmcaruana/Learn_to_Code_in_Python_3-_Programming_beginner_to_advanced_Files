months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

birthday = input("Please enter your date of birth in the format DD-MM-YYY: ")

index = int (birthday [3:5])-1
bd_month = months[index]

print("You were born in", bd_month)

people = ["John", "Mary", "Peter"]

user = input("Type your name: ")
people.append(user)
print("Here's the list: ",people)

