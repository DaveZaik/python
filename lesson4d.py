# create a funxction to calc te BMI value of a person x
# print the height, weight and BMI Value
# formulae
# BMI=weight/height**2
def BMI():
 height=float(input("Enter Height in meters: "))
 weight=int(input("Enter weight in kgs: "))
 BMI=weight/height**2
 print(BMI)

 if BMI >=18.5 and BMI<=22.9:
  print("Normal")

 elif BMI <18.5:
   print("Underweight")

 elif BMI >=23 and BMI<=24.9:
  print("Overweight")

 elif BMI >=25 and BMI<=29.9:
  print(" Pre-Obese") 

 elif BMI >=30 and BMI<=34.9:
  print("Obese class I")

 elif BMI >=35 and BMI<=39.9:
  print("Obese class II")

 elif BMI >=40.0:
  print("Obese class III")

 else:
  print ("Invalid Input")
  
# BMI()

# area of a circle
# parameters
def Area_circle(radius):
   area_circle=3.14*radius**2
#    print (f"The area of circle with radius {radius} is {area_circle}" )
   return area_circle

# Area_circle (7)
print("the area of a circle is",Area_circle(7))

# More than one parameter
def Total_marks ( name,maths,eng,kisw,chem,hist):
 total = maths + eng+kisw+chem+hist
 print(f"{name} got a total marks of {total} in the closing exams")
 return total
Total_marks("Kevin",87,65,78,97,81)

# error handling(try,except)
# object oriented programming in python