"""
for number in range(1, 10, 2):
    print("Attempt, ", number, number * ".")

"""
"""
# for else:


successful = True
for num in range(3):
    print("try")
if successful:
    print("Successful")
    
else:
    print("Unsuccessful")

"""
"""
for x in range(5):
    for y in range(3):
        print(f"(x={x}),y={y}")
        
"""


#         0
#        000
#       000000
#     0000000000
#    000000000000
#   00000000000000
        
pyrmaid_witdh = 10

for i in range(0, pyrmaid_witdh):
    for j in range(0, pyrmaid_witdh-i):
        print(" ", end ="")
    for k in range(0, 2*i+1):
        print("0", end ="")
    print("")

    
# depends on i first loop


# mylist = iter(["apple", "banana", "cherry"])
# x = next(mylist, "orange")
# print(x)
# x = next(mylist, "orange")
# print(x)
# x = next(mylist, "orange")
# print(x)
# x = next(mylist, "orange")
# print(x) 



