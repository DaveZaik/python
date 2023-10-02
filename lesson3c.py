# check if someone qualifies for blood donation
age=int(input("Enter Age: "))
weight=int(input("Enter weight in kgs: "))
blood_pressure=int(input("Enter blood in kgs: "))
if age >=18 and age <=80:
    # check the second condition
    if weight >=50:
        print("Qualifies to Donate Blood")
        # check for other conditions
        if blood_pressure <=95 and blood_pressure >=80:
            print("Blood pressure hig or too low")
    else:
        print("The person is Underweight")
else:
    print("The person is underage")