# create two dictionaries and join them 
# first dictionary is for first child  and second for second Child
# the properties are Name, Age ,Level of education for both dictionaries
# create a dictionary inside another dictionary
Family ={
    "child1":{
    "Name":"Kevin",
    "AGE":17,
    "EDUCATION lv":" HIGH SCHOOL"
    },
    "child2":{
    "Name":"GWEN",
    "AGE":20,
    "EDUCATION lv":" UNI"
}
 }
print(Family)

child1 ={
    "Name":"DAN",
    "AGE":17,
    "EDUCATION lv":" HIGH SCHOOL"
    }
child2 ={
    "Name":"GWEN",
    "AGE":20,
    "EDUCATION lv":" UNI"
}
family1={
    "child1":child1,
    "child2":child2
}
print(Family)
print(family1)