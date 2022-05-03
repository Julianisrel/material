import string
# The string module is really helpful when you have questions involing Strings
#ASCII code - basically a mapping beteen chracters and numbers
# Example: ord('A') -> 65 , ord('a') -> 97 Compare 'A' > 'a' -> False
# 'abc' > 'abd'
# False

# print('HEllO'.isupper())
# -> False  



string.ascii_uppercase

def is_upper(char):
    for letter in char:
        if letter not in string.ascii_uppercase:
            return False
    return True

# print(is_upper('HELLO'))
# print(is_upper('Hello'))

# now with set()
uppercase_set = set(string.ascii_uppercase)
def is_upper_using_set(char):
    for letter in char:
        if letter not in string.ascii_uppercase_set:
            return False
    return True

# print(is_upper('HELLO'))
# print(is_upper('Hello'))

# %timeit - method that finds the time it takes to run a function

# %timeit is_upper('HELLO')


uppercase_set = set(string.ascii_uppercase)
# now cleaner way to do it
# all() - checks if all the elements in the iterable are true

def is_upper_cleaner(s):
    return all(letter in uppercase_set for letter in s)

print(is_upper_cleaner('HELLO'))
print(is_upper_cleaner('hello'))
all(print(5) for _ in range(5))

string.ascii_letters
string.ascii_uppercase
string.ascii_lowercase
string.digits
string.hexdigits
string.octdigits
string.punctuation
string.printable
string.whitespace