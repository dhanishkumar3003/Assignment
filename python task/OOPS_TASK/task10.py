# 9-1. Restaurant: Make a class called Restaurant. The init() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.
# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

#9.1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open!")

restaurant = Restaurant("Pasta Palace", "Italian")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9.2

restaurant1 = Restaurant("Mani's Dum Biriyani", "Indian")
restaurant2 = Restaurant("Food Paradise", "Chinese")
restaurant3 = Restaurant("Dominos", "American")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#9.3
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        print(f"User Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

user1 = User("Dhanish", "Kumar", 22, "Porur", "dhanish@gmail.com")
user2 = User("Basil", "Ahemad", 22, "Navalur", "basil@gmail.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
