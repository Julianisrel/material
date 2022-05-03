"""
DICTONARIES & .collections.DEFAULT DICTIONARIES
"""

from email.policy import default


student_grades = {
    "jack": [85, 90],
    "jill": [80, 95],
    "julz": [75, 100],
}

def get_grades_naive(student):
    if student in student_grades:
       return student_grades[student]
    return []

# print(get_grades_naive("jack"))
# print(get_grades_naive("jill"))
# print(get_grades_naive("julian"))

# BETTER WRITTEN FUNCTION THAN FROM ABOVE USING THE GET METHOD FUNCTION
# default method
def get_grades_better(student):
    return student_grades.get(student, [])

# print(get_grades_better("jack"))
# print(get_grades_better("jill"))
# print(get_grades_better("julian"))


def get_grades_with_assigment(student):
    if student not in student_grades:
        student_grades[student] = []
    return student_grades[student]

# defalut method
# .setdefault
# get funcitons
def get_grades_with_assigment_better(student):
    return student_grades.setdefault(student, [])

# print(get_grades_better("julz"))


# Set method - is used to convert any of the iterable to sequence of 
# iterable elements with distinct elements, commonly called Set.

def set_grade_naive(student, score):
    if student in student_grades:
       grades = student_grades[student]
    else:
        student_grades[student] = []
        grades = student_grades[student]
    grades.append(score)


set = set_grade_naive("julz", 200)
# print(student_grades)

# output - {'jack': [85, 90], 'jill': [80, 95], 'julz': [75, 100, 200]}


# better way now
def set_grade_better(student, score):
    grades = []
    get_grades_with_assigment_better(student)
    grades.append(score)

#simplify it more with deafult method


from collections import defaultdict

student_grades = defaultdict(list, student_grades)

def set_grade_best(student, score):
    student_grades[student].append(score)

set_grade_best("julz", 200)
print(student_grades)
"""
output: defaultdict(<class 'list'>, {'julz': [200]})
"""

# KEEP PRACTING THIS SHIT