import json
import requests

# first_name = "Eloka" # this is a comment
# age = 24
# test_score = 93.4
# owns_a_car = True

# shopping_list = [
#     "fruit", "meat", "eggs"
# ]

# shopping_list.pop(1)
# shopping_list.append("bread")

# # Dictionaries

# dictionary = {
#     "happy": "To be content with everything",
#     "sad" : "To be not content"
# }


# dictionary.pop("happy")

# dictionary["angry"] = "To be furious ..."

# dictionary.update({
#     "excited" : "energised in a dynamic way",
#     "nervous" : "axnious in anticipation of a future event"
# })


# # Conditionals

# if x > 5:
#     print("X is greater than 5")
# elif x < 5:
#     print("X is smaller than 5")
# else:
#     print("X is 5")


# # Loops

# names = ["matt", "eloka", "nyasha"]

# for name in names:
#     print(name)

# # Functions

# def full_name(first_name, last_name):
#     return first_name + " " + last_name

# result = full_name("Eloka", "Agu")
# result2 = full_name("Michael", "Jackson")


# print(result)
# print(result2)

# # Classes

# class House:    
#     rooms = None
#     bathrooms = None
#     has_garage = None


#     def __init__(self, num_rooms, num_bathrooms, has_garage):
#         self.rooms = num_rooms
#         self.bathrooms = num_bathrooms
#         self.has_garage = has_garage

#     def total_num_of_rooms(self):
#         return self.rooms + self.bathrooms
    
# matts_house = House(num_rooms=2, num_bathrooms=1, has_garage=False)
# joes_house = House(num_rooms=4, num_bathrooms=2, has_garage=True)

# class Hotel(House):
#     pass

# dudes_hotel = Hotel(num_bathrooms=2, num_rooms=3, has_garage=False)

person = {
  "name": "John",
  "lastName": "Doe"
}


string_person = json.dumps(person)

result = json.loads(string_person)

response = requests.get("https://jsonplaceholder.typicode.com/todos")

todos = response.json()

for todo in todos:
    print(todos[0])