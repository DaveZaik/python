# for loops
# looping through a tuple
#  create a tuple of countrries in africa
Africa=("Kenya","Tanzania","Uganda","Rwanda","Nigeria")
for country in Africa:
    # check if the country is Uganda and break the loop
    if country=="Uganda":
        break #terminating the loop
    print(country)

# continue
for country in Africa:
    if country=="Uganda":
        continue
    print(country)