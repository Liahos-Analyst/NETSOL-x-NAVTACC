# Week 2 | Class 01: Functions, scope, lambda, map, filter and exceptions
# References:
# https://www.geeksforgeeks.org/functions-in-python/
# https://www.programiz.com/python-programming/exception-handling
# https://www.programiz.com/python-programming/user-defined-exception

tax_rate = 0.05  # global scope

def invoice(amount, tax=tax_rate):
    """Return amount plus tax."""
    total = amount + amount * tax
    return total

def make_multiplier(factor):
    def multiply(value):
        return value * factor
    return multiply

double = make_multiplier(2)
numbers = [1, 2, 3, 4, 5]
print("Invoice:", invoice(1000))
print("Double 7:", double(7))
print("Squares with map:", list(map(lambda x: x * x, numbers)))
print("Even values with filter:", list(filter(lambda x: x % 2 == 0, numbers)))

try:
    value = float(input("Enter a number: "))
    print("Reciprocal:", 1 / value)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Zero has no reciprocal.")

class InvalidAgeError(Exception):
    pass

def register_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    return f"Age {age} accepted."

try:
    print(register_age(20))
except InvalidAgeError as error:
    print(error)
