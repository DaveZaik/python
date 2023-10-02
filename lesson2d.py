# dictionary
# defined using curly braces
# ordered
# mutable
# accept multiple dat types
# pairs (key and a value)
# does not accept duplicates
car={
    "Name":"Aston Martin",
    "Model":"Victor",
    "Country":"United Kingdoms",
    "YOM":2021,
    "colours":["Blue","Black","White"]
}
print(car)
print(car['Name'])

# change the model of car
car["Model"]="DB9" # update
print(car)
print(car['Name'])

print(car.keys()) # access the keys only
print(car.values()) # access the values

# access the colours
print(car['colours'][1])

# create two dictionaries and join them 
# first dictionary is for first child  and second for second Child
# the properties are Name, Age ,Level of education for boyth dictionaries
# create a dictionary inside another dictionary
