from functools import reduce

# reduce - is a function that helps combine or reduce an iterable to a single value.
# print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
# Output: 10
# intial value of 10
print(reduce(lambda x, y: x * y, [1, 2, 3, 4], 10))
# so reduce did - ((((10 * 1) * 2) * 3) * 4)
# important to include the parathes from left to right to show it didn't do it all at once

# So in a INTERVIEW if asked to some how combine a list into one value then functools.reduce should
# come to mind


# decractors 

# look up docs for decorators