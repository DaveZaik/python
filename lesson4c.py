# python functions
def greet():
    print("Wassup my nica!")
    # sum
    numbers=(43,45,65)
    sum_numbers=sum(numbers)
    print("The sum of numbers is",sum_numbers)

    len_numbers=len(numbers)
    print("the lenth of numbers is",len_numbers )
# call function
greet()

def Student_details():
    name =input("Enter name of student:")
    age =int(input("Enter Age of student:"))
    grade =input("Enter the Year:")
    school=input("Enter the school of student:")

    print(f"{name} is {age} years old and he is on his {grade} year at {school}.")
Student_details()