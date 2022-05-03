from collections import namedtuple


# Collection.namedtuples - Are a subclass of tuples which really helps if 
# want to define a immutable classes

Car = namedtuple('Car',["color","make","model", "mileage"])
# print(Car)

Car1 = Car("red","bmw","550i", "15")
# print(Car1)

# access arttibute of class tuple
my_car = Car(color="red", make="bmw", model="550i", mileage="15")
# print(my_car.color)
# print(my_car.make)
# print(my_car.model)
# print(my_car.mileage)

print(my_car[0])




