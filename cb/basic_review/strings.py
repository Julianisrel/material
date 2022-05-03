# Reverse a string
def solution(string):
    new_str = string[1::-1] and string[::-1]
    return new_str
# return [::-1]

#  test
import test  
from solution import solution

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(solution('world'), 'dlrow')
        test.assert_equals(solution('hello'), 'olleh')
        test.assert_equals(solution(''), '')
        test.assert_equals(solution('h'), 'h')

# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else: 
        if boolean == False:
            return "No"
         