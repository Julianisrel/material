from collections import defaultdict
from collections import Counter

def top_three_letters(string):
    """
    Given a string find the top three most common letters in the string.
    This method should return a list of tuples. Each tuple should contain
    the character and count.
    
>>> top_three_letters("abbccc")
[('c',3), ('b',2), ('a',1)]
>>> top_three_letters("aabbccd")
[('a',2), ('b',2), ('c',2)]
"""
    # Your code here:
    # loop through the string
    # sort the dictionary by the count and find the top 
    # three most fequent letters
    # return a formatted list to match the output
    
    #   int() is a function when called return 0 so are default will be 0
    
    # counter = defaultdict(int)
    # for char in string:
    #     counter[char] += 1
    # print(counter) - make sure the loop is working correctly
    # top_three = sorted(counter, key=lambda k: counter[k], reverse=True)[:3]
    # print(top_three) #- made sure the str reverse is working slice in half
    
    # result = []
    # for letter in top_three:
    #     result.append((letter, counter[letter]))
   
    # list comprehension
    # return [
        # (letter, counter[letter]) for letter in top_three
    
    # ]
    


# *******************************************************************************
# Now write this in one line using built-in counter class 
# Counter class is a dictionary like object that counts hashable objects

    return (Counter(string).most_common(3))





