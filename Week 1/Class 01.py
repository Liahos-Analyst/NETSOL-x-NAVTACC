# Week 1 | Class 01: Python basics, variables, types, input, operators
# Based on the NAVTTC course plan: values, expressions, strings, input and type casting.

name = input("Your name: ").strip() or "Learner"
age_text = input("Your age: ").strip()
age = int(age_text) if age_text.isdigit() else 18

print(f"\nHello, {name}!")
print("Next year you will be", age + 1)

# Core data types
integer_value = 12
float_value = 3.5
text_value = "Python"
boolean_value = True

print("\nTypes:")
for value in (integer_value, float_value, text_value, boolean_value):
    print(value, "->", type(value).__name__)

# Arithmetic and comparison operators
a, b = 17, 5
print("\nArithmetic:", a + b, a - b, a * b, a / b, a // b, a % b, a ** 2)
print("Comparisons:", a > b, a == b, a != b)

# String operations
message = "  Learn Python for AI  "
print("\nUpper:", message.upper())
print("Lower:", message.lower())
print("Clean:", message.strip())
print("Replace:", message.replace("AI", "data science"))
print("Words:", message.split())

# Small practice task
price = float(input("\nEnter product price: "))
quantity = int(input("Enter quantity: "))
print(f"Total cost: {price * quantity:.2f}")
