# There are also some useful built-in functions that can be applied to lists such as max(), min(), any(), and all():

# max() finds the maximum value of an iterable using the built-in cmp() method, or the key param.
# min() finds the minimum value of an iterable using the built-in cmp() method, or the key param.
# any() returns whether any of the elements in the iterable are a true value.
# all() returns whether all of the elements in the iterable are true values.

from importlib_metadata import method_cache
from sqlalchemy import column


# list = [1,2-5,4]

def square(x):
    return x * x


# print(list(map(square, lst)))

# for num in (lst):
#     result = []
#     result.append(square(num))
    # print(result)

# list Comprehension

# print([(lambda multi: x * x )(x) for x in [1, 2, -5, 4]])

# They’re used in place of functions like map() and filter(). 
# To learn more, check out Using List Comprehensions Effectively.


# filters out the odd number from the list
# fliter() method - filters out the odd number from the list 
lst = [1,2,3,4,5,6,7,8,9,10]
def is_odd(int):
    return int % 2 == 1

# print(list(filter(is_odd, lst)))

# list_comp - version
# print([num for num in lst if is_odd(num)])

# commomn like interview question matrix
# rows 4 & columns 3
grid = [[1, 2, 3, 4], 
        [5, 6, 7, 8],
        [9, 10, 11, 12]]


# print([row[1] for row in grid])
"""
Some helpfu methods from the top:
"""
list = [1,2,-5,4]
# print(max(list))

# find the largest sqaure of list
"""
print(max(list, key=square))
"""

"""
# find smallest sqaure number in list
# print(min(list))
"""
# print(min(lst, key=lambda x: x**2))
# print(min(list, key=square))

"""
any method - any() returns whether any of the elements in the iterable are a true value.

"""
lst = [1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
# (bool(2 in lst))
# print(any(lst))

# check values in list are odd
# print([(lambda x: x % 2 == 1)(num) for num in lst])
# print(any([(lambda x: x % 2 == 1)(num) for num in lst]))
# print(all([(lambda x: x % 2 == 1)(num) for num in lst]))





