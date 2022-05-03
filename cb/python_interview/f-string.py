age = 10

name = 'jay'

# .format
# print("my name is {name} and I am {age} years old".format(name=name, age=age))

# f-strings
print(f"my name is {name} and I am {age + 5} years old")


class A(object):
    def __init__(self, name):
        self.name = name
        self.age = age
        def __repr__(self):
            return f"""
                My name is {self.name}.
                I am {self.age} years old.
                """

    print(A(name, age))

        # My name is jay.
        # I am 15 years old.
# mulitine string


