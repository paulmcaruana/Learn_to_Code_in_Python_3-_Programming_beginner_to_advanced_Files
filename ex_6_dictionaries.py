person = {"name": "Paul", "gender": "male", "age": 46, "address": "9 Ashmore Road", "phone": "07437010710"}

key = input("What information would you like to know? ").lower()

result = person.get(key, "key not found")

print(result)

