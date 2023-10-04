class Car:
    # properties
    color = "white"
    name = "BMW"
    cc = 3000
    
    # functions
    def drive(self):
        print("Driving this car is interesting")
    
    def speed(self):
        print("Very fast car")
    
    def start(self):
        print("Car has been started successfully")
    
    def stop(self):
        print("The car is stopping")

my_object = Car()
print(my_object.name)  # Accessing the properties
# Accessing the function
my_object.start()
