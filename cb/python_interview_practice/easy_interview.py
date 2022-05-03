# from collections import Counter
# def majority_element_indexes(lst):
#     '''
#     Return a list of the indexes of the majority element.
#     Majority element is the element that appears more than
#     floor(n / 2) times.
#     If there is no majority element, return []
#     >>> majority_element_indexes([1, 1, 2])
#     [0, 1]
#     >>> majority_element_indexes([1, 2])
#     []
#     >>> majority_element_indexes([])
#     []
#     '''

# # your code here 
# # Find the majority element
# # If there is no majority element, return []
# # Find the indexes of the majority element

#     # solution

#     if lst == []:
#         return []

#     count = Counter(lst)
#     top_elems = sorted(
#         count.keys(),
#         key=lambda x: -count[x],
#     )
    

#     majority_elem = top_elems[0]
    
#     # there exist a majority element
#     if count[majority_elem] > len(lst) // 2:
#         return [
#         i for i, elem in enumerate(lst) if elem == majority_elem
        
#         ]
#     else:
#         return []
# print(majority_element_indexes([1,1,2]))
# print(majority_element_indexes([1,2]))
# print(majority_element_indexes([]))

# Steps 
# Find the majority element
# # If there is no majority element, return []
# # Find the indexes of the majority element
# time anyalyis  - 

from collections import Counter

def majority_element_indexes(lst):
    if lst == []:
        return []
    count = Counter(lst) #- takes O(n) time because it has to iterate through the list and build a dictionary
    top_elems = sorted( #- top_elems sorted always takes n(log n)for anything
        count.keys(),   # - where n is the length of the iterateble passing in and the key dosen't effect the run time 
        key=lambda x: -count[x],
        # O(n log n)
    )
    

    majority_elem = top_elems[0] #- O(1) constant time
    
    # there exist a majority element
    if count[majority_elem] > len(lst) // 2:  #- O(1) constant time
        return [
        i for i, elem in enumerate(lst) if elem == majority_elem
        
        ] # - n time
    else:
        return []



# way to speed this up 
# instead of sorting the list, you can use a hash table
# where the lambda fucntion would be 
top_count = max(count.values()) #O(n)
maj_elem = [elem for elem, count in count.item() == top_count][0]
#O(n) time

# O(n) + O(n) = O(n)