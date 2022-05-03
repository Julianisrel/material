# matrix 
# 2d lists
# row's comes first
# column's 2nd
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
# print(number_grid[2][2])



# for row in number_grid:
#     for column in row:
#         # print(column, end=", ")

# number = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16]
# ]

# # for rows in number:
# #     for col in rows:
#         # print(col, end=",")



# # Backtracking is a recursive algorihim

# # List = [1,2,3,4,5,6,7,8,9,10]
# # print(number[::-1])


# s_array =[[16], [11, 12, 13, 14, 15], [6, 7, 8, 9, 10], [1, 2, 3, 4, 5]]



# # print(s_array([0, 4]))


# # itertools
# # iter() -function method
# # next() -> method function
# # count
# # repeat
# # cycle 


 

# # r = range(1, 11)
# # i = iter(r)

# # print(list(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))


# # itertools modules - meaning thery can return an infinte sequnece
 
# # infinte intertools ,squence

# from itertools import count
# from itertools import repeat
# from itertools import cycle
# from itertools import accumulate 
# from itertools import chain 


# # def count_example(start, step):
# #     counter = count(start, step)

# #     for c in counter:
# #         print(c)
    
# #         if c == 100:
# #             break


# # count_example(10, 5)

# # def repeat_example(element, max_repeats):
# #     repeater = repeat(element, max_repeats)

# #     for val in repeater:
# #         print(val)
    
        

# # repeat_example("hello", 5)

# # def cycle_example(element):
# #     i = 0
# #     cycler = cycle(element)

    

# #     while i < 100:
# #         print(cycler)
# #         print(next(cycler), end =", ")
# #         i += 1

# # cycle_example("ABCDEF")




# # terminating Iterators
# # accumulate

# # def accumulate_example(elements):
# #     running_sum = accumulate(elements)
# #     print((list(running_sum)))


    
    

    
# # accumulate_example([1,2,3,4,5,6,7,8,9,10])

# # def chain_example(element1, element2):
# #     chained = chain(element1, element2)
# #     print(list(chained))


    
    

    
# # chain_example("ABC", "DEF")


# def chain_fromexample(element1, element2):
# #     chained = chain(element1, element2)
# #     print(list(chained))


    
    

    
# chain_example("ABC", "DEF")


# Python code to demonstrate 
# decode() 
    
# initializing string  
# str = "geeksforgeeks"
    
# # encoding string  
# str_enc = str.encode(encodeing='utf8') 
    
# # printing the encoded string 
# print ("The encoded string in base64 format is : ",) 
# print (str_enc )
    
# # printing the original decoded string  
# print ("The decoded string is : ",) 
# print (str_enc.decode('utf8', 'strict'))



# st1 = 'Julian'
# str_enc = str1.encode(encodeing='utf8')

# print(str_enc)



a = [0,1,2,3]
for a[-1] in a:
    print(a[-1])


# proramize the code
A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]


print("A =", A) 
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

column = [];        # empty list
for row in A:
  column.append(row[2])   

print("3rd column =", column)
"""
When we run the program, the output will be:
A = [[1, 4, 5, 12], [-5, 8, 9, 0], [-6, 7, 11, 19]]
A[1] = [-5, 8, 9, 0]
A[1][2] = 9
A[0][-1] = 12
3rd column = [5, 9, 11]




"""
