animals = ["cat", "dog", "rabbit", "turtle", "snake"]

# print(sorted(animals, reverse=True))

# index is from 0,2 bottom to top 
animals = [
    {"type": 'cat', 'name': 'fluffy', 'age': 2 },
    { "type": 'dog',  'name': 'spot', 'age': 1},
    {"type": 'rabbit', 'name': 'carrot', 'age': 3}
]
# dict sorted by age
# print(sorted(animals, key=lambda animal: animal['age']))
# print(sorted(animals, key=lambda animal: animal['age'], reverse=True))

# get oldest animal
# print(sorted(animals, key=lambda animal: animal['age'], reverse=True)[0])


# sort() method will mutate the list 
# print(animals.sort(key=lambda animal: animal['age']))

