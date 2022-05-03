# range() is a built-in function used to iterate through a sequence of numbers. Some common use cases would be to iterate from the numbers 0 to 10:


# enumerate() is a built-in function to iterate through a sequence 
# and keep track of both the index and the number. 
# You can pass in an optional start parameter to indicate 
# which number the index should start at:

# list - function -The list() constructor returns a list in Python.
# Example
# convert string to list


text = 'Python'
text_list = list(text)



# enumerate() in action 
# index - 0,1,2
# number - 123
# print(list(enumerate([1, 2, 3])))
# print(text_list)

"""
Given a list of intergers:
1.  Replace all integers(numbers) that are currently disvible by 3 with the string 'Fizz'
2.  Replace all integers that are currently disvible 5 with the string 'Buzz'
3.  Replace all integers that are currently disvible by both 3 and  5 with the string 'fizzBuzz'

>>> numbers = [45,22,14,65,97,72]
>>> fizz_buzz(numbers)
>>> ['fizz_buzz', 22, 14, 'buzz', 97, 72]

"""
# 1, check if the number is divisible by 3
# 2, check if the number is divisible by 5
# 3, check if the number is divisible by both 3 and 5
# modulo Operator allows you to check if a number is divisible by another number.


def fizz_buzz(numbers):
    for i, num in enumerate(numbers):
        if num % 5 == 0 and num % 3 == 0:
            numbers[i] = "fizzbuzz"
        elif num % 3 == 0:
            numbers[i] = "fizz"
        elif num % 5 == 0:
            numbers[i] = "buzz"

    return numbers

numbers = [45,22,1,4,65,97,72]
print(fizz_buzz(numbers))
# passtest