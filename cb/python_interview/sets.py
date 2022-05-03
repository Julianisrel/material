"""
 SETS are unsorted collections that allows for adding, removing, and 
 checking membership in constant time. 
 They do not allow duplicates.
  Here's an example:
"""

# doctest - only gives output if there are errors

# not using a set
# count_unique function counts the number of unique elements in a string
# and returns the number of unique elements

#  This fuciton is O(n^2)
def count_unique(s):
    """
    Count number of unique characters in s
>>> count_unique("aabb")
2
>>> count_unique("abcdef")
6
    
   """

    seen_c = [] # o(1) 
    for c in s: # O(n) time 
            if c not in seen_c: #O(n)
                seen_c.append(c) # O(1)
    return len(seen_c) # O(n^2)


#  Using set 
# def count_unique2(s):
#     seen_c = set() 
#     for c in s:
#         if c not in seen_c: 0(1)
#             seen_c.add(c)
#     return len(seen_c)

# return len({c for c in s}) # O(n)

# return len(set(s)) # O(n)

