# iter() method - 
# it.permutations - Permutations means different orders by which elements can be arranged. The elements might be of a string, or a list, or any other data type. It is the rearrangement of items in different ways. Python has different methods inside a package called itertools, which can help us achieve python permutations

import itertools as it


# all_ones = it.repeat(1)
# print(all_ones)
# print(next(all_ones))



# create a list of 10 and ^2 each number

"""
print(list(map(pow, range(10), it.repeat(2))))

print(list(map(pow, range(10), it.repeat(3))))


print(list(map(pow, range(10), it.repeat(4))))
"""
# A easy way to have a constant stream of mubers you need to keep accessing over and over
# more methods
# all_ones = it.count(1,times=5)
# list(all_ones)

# it.cycle

# alternationg_ones = it.cycle([1,-1])

friends = ['jay', 'juls', 'julian']
# print(list(it.permutations(friends, r=2)))

# stop when you get to julian
print(list(it.combinations(friends, r=3)))



# should ask interviewer if it;s okay to use these built in methods becuase sometime they 
# may want you to build-it from scratch


