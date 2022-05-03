# Generators are used for iterating over a sequence of values.
# Reason to use gernators is to avoid the creation of a list of all the values in a sequence.
"""
g = (i for i in range(6))

print(next(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

"""




# print(sum([i for i in range(1, 1001)]))
from email import generator
import sys
iterators = iter((i for i in range(1, 1001)))
# print(next(iterators))
# print(next(iterators))
# print(next(iterators))
# print(next(iterators))

# lst = [i for i in range(1, 1001)]
# print(sys.getsizeof(lst))


g = (i for i in range(1, 1001))
print(sys.getsizeof(g))

# So in a interview if asked to iterate through soemthing with a lots of values,
# you can use generators. Also you a generator if don't need to evaluate all the values in the sequence.


# another e.g.



