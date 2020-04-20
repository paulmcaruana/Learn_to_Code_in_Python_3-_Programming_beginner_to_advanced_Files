
data_valid = False

while data_valid == False:
        grade1 = input("Type the grade of your first test: ")
        try:
                grade1 = float(grade1)
        except:
                print("please use a valid number")
                continue
                
        if grade1 < 0 or grade1 > 10:
                print("Grade should be between 0 and 10")
                continue
        else:
          data_valid = True

data_valid = False

while data_valid == False:
        grade2 = input("Type the grade of your second test: ")
        try:
                grade2 = float(grade2)
        except:
                print("please use a valid number")
                continue

        if grade2 < 0 or grade2 > 10:
                print("Grade should be between 0 and 10")
                continue
        else:
                data_valid = True
      
data_valid = False

while data_valid == False:
        total_classes = input("Type the total number of classes: ")
        try:
                total_classes = int(total_classes)
        except:
                print("please use a valid number")
                continue

        if total_classes <=0:
                print("The number of classes can't be zero or less")
                continue
        else:
                data_valid = True

data_valid = False

while data_valid == False:
        abscences = input("Type the number of abscences: ")
        try:
                abscences = int(abscences)
        except:
                print("please use a valid number")
                continue

        if abscences <0 or abscences > total_classes:
                print("The number of abscences can't be less than zero or greater than the total number of classes")
                continue
        else:
                data_valid = True
                


avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - abscences) / total_classes

print("Average grade: ", round(avg_grade,2))
print("Attendance rate: ", str(round((attendance * 100),2))+"%")

if (avg_grade >= 6 and attendance >= 0.8):
        print("The student was approved.")
elif (avg_grade <= 6 and attendance <= 0.8):
    print("The student has failed due to an average grade lower than 6 and an attendance rate lower than 80%")
elif (attendance >= 0.8):
        print("The student has failed due to an average grade lower than 6.0")
else:
    print("The student has failed due to an attendance rate lower than 80%")
