firstName = str(input("Please enter your first name: "))
secondName = str(input("Please enter your second name: "))

print("Your initials are " + firstName[0] + secondName[0] + ".")

lotNumber = "037-00901-00027"

print("Country code: " + lotNumber[:3])
print("Product code: " + lotNumber[4:9])
print("Batch Number: " + lotNumber[-5:])
