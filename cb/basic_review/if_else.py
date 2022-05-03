

# temp = 35

# if temp > 40 or temp < 10:
    # print("It's hot outside")
# else:
    # print("It's not hot outside")



# high_income = False
# good_credit = True
# student = True


# if high_income or good_credit and not student:
    # print("Eligible for loan")
# else:
    # print("Not eligible for loan")


# Chaining Compaarison operators


#  age should between 18 and 65

# age = 25 

# if age >= 18 and age < 65:
    # print("let inside the party")

# quiz 

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat": #letter in alphabetical order
    print("b")
else:
    print("c")
# ------------------------------------------------------
# In this simple assignment you are given a number and have to make it negative. 
# But maybe the number is already negative?

def make_negative( number ):
    if (number >0):
        return -number
    elif number < 0:
        return number
    else:
        return 0
# from solution import make_negative

# @test.describe("Fixed Tests")
# def basic_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(make_negative(42),-42)
#         test.assert_equals(make_negative(-9),-9)
#         test.assert_equals(make_negative(0),0)


# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".
def greet(name):
    return f"Hello, {name} how are you doing today?"
 
    # caluclte array 
def find_average(array):
    return sum(array) / len(array) if array else 0



