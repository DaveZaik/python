# logical operators
# input function
marks= int (input("Enter marks for student:"))
if marks >0 and marks <=40:
    print ("Fail" )
elif marks >40 and marks<=50:
 print("Grade D")
elif marks >50 and marks<=60:
 print("Grade C")
elif marks >60 and marks<=70:
 print("Grade B")
elif marks >70 and marks<=100:
 print("Grade A")
else:
  print("invalid marks")
    