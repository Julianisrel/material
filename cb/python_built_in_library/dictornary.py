# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 2022
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary") 


my_dict = {
  "brand": "civic si",
  "model": "Honda",
  "year": 2022
  }


access_dict = my_dict["model"]
change_dict = my_dict["brand"] = "Nissan"
change_dict_year = my_dict["year"] = 2020

# print(change_dict_year)
# print("key: change_dict", change_dict)
# print("key: access_dict", access_dict)



people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

# print(people[0]['name'])
# print(people[1]['age'])
# print(people[2]['sex'])

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  