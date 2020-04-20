print("This program calculates your body mass index(bmi)")

weight = float( input("Please input your weight in kgs: "))
height = float( input("Please input your height in metres: "))

BMI = weight/(height*height)

print("Your BMI is ", round(BMI, 1))

if (BMI <= 18.5):
       print("You are underweight")

elif (BMI > 18.5 and BMI <= 24.9):
    print("You're weight is normal")

elif (BMI > 24.9 and BMI <= 29.9):
    print("You are overweight")

else:
    print("You are obese")
