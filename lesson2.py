# Python lists
# Properties
# Defined using square brackets []
# Contains items of diffeefrent data types
# Mutable /changable
# Ordered-individual items in the list can be accessed
# Can be updated (add and delete items frrom the list)

#list of programming languages
languages=["HTML","CSS", "Kotlin", "Python", "Javascript"]
print(languages)
print(type(languages))

#Access the first item(ordered)
print(languages[0])

#print a range
print(languages[0:3])

#change
languages[0]="Java"
print(languages)

#update
#append
languages.append("C#")
print(languages)

#Create another list
new=("Data Science","Cyber Security", "Business Administration")
languages.extend(new)
print(languages)

#delete
languages.pop(0) #index
print(languages)

#remove
languages.remove("Business Administration")
print(languages)






