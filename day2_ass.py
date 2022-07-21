#Assignment. 
print("Week 3-day 2, Assignment")

#   Create an class called car
# Give 5 attributes of the car class
# Give 5 methods of the car class
# Ensure the class is working as expected
# Push your code to github 

#giving the attribute using construction method
class Car:
    def __init__(self, tyre_type, engine, fuel_type, body_colour, door):
        self.tyre = tyre_type
        self.engine = engine
        self.fuel_type = fuel_type
        self.body_colour = body_colour
        self.door = door

# creating instance of class
toyota_matrix = Car("Bridgestone", "four cylinder", "Petrol", "red", 4)

#Another instance of class
venza = Car("Pirelli", "four cylinder", "diesel", "white", 4 )

#priniting attribute from first instance
print("\nToyota matrix has ",toyota_matrix.tyre,"tyres", 
", the engine is of ", toyota_matrix.engine,
", the car set coluur is:",toyota_matrix.fuel_type,
", the colour of the car is:", toyota_matrix.body_colour,
", it has ",toyota_matrix.door, "doors")


#printing attribute fro second instance 
print("\n",venza.tyre, ":", venza.engine, ":", venza.fuel_type,":", venza.body_colour, ":",venza.door)

