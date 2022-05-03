# slicing ls


def rotate_left3(nums):
    rotate = nums[1:]
    rotate.append(nums[0])
    return rotate



print(rotate_left3([1, 2, 3])