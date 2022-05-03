"""

Dictionary elements must be accessible somehow. If you don’t get them by index, then how do you get them?

A value is retrieved from a dictionary by specifying its corresponding key in square brackets ([]):





"""



Dicts = {
     'key1': 'value1',
     'key2': 'value2',
     'key3': 'value3',
     'key4': 'value4',
     'key5': 'value5',
 }



# get() method- returns the VALUE of the specified key.
"""
print("Value : %s" %  Dicts.get('key3'))
print("Value : %s" %  Dicts.get('key1', "value1"))
"""



# access by key
# print(Dicts['key1'])


# Adding an entry to an existing dictionary is simply a matter of assigning a new key and value:

new_entry = Dicts['key6'] = 'value6'
# print(new_entry)


# To delete an entry, use the del statement, specifying the key to delete:

del Dicts['key6']

"""
Dictionary Keys vs. List Indices and lists
"""
# nested and mutable list in dict
student = {'name': 'Jay', 'age': 25, 'courses': ['Math', 'CompSci']}

# print(student['courses'])


"""
 Looping through dict using iterator items() method
 """

for key, value in Dicts.items():
    print(key, value)