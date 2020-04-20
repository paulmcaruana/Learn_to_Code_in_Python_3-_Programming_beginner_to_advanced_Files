import math

radius = float(input("what is the radius of your circle: "))

area = math.pi * (radius**2)
circumference = 2 * math.pi * radius

print("The area of your circle is: ", round(area,2), " and the circumference is: ", round(circumference))

