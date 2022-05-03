# debugging with print statemnt 
"""
def maxNumber(lst):
    max_num = 0 
    for num in lst:
        print('postion', num, 'max_num', max_num)
        if num > max_num:
            print('entered if statemnt')
            max_num = num
    return max_num
"""
# print(maxNumber([-1,-2,-4]))
"""
outout: postion -1 max_num 0
postion -2 max_num 0
postion -4 max_num 0
0
"""

# built-in debugger

def maxNumber(lst):
    max_num = 0 
    for num in lst:
        breakpoint()
        if num > max_num:
            max_num = num
    return max_num

print(maxNumber([-1,-2,-4]))

