# list
# tuple
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
