# Classes are user defined blueprint or prototype
# Class have methods, class variables,instance variables, constructor, etc
# Self keyword is mandatory for calling variable names into method
# Instance and class variables have whole different purpose(1 is attached to object & 1 is not attached to object)
# Constructor name should be __init__
# New keyword is not required when you create object


class Calculator:
    num = 59  # Class Variable

    # Default Constructor
    def __init__(self, a, b):
        self.firstNumber = a      # Instance variable
        self.secondNumber = b     # Instance variable
        print("I am called automatically when object is created")

    def getData(self):
        print("I am executing as Method in Class")

    def number(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(5, 9)   # Syntax to create objects in python
obj.getData()
print(obj.number())

obj1 = Calculator(5, 5)   # Syntax to create objects in python
obj1.getData()
print(obj1.number())


