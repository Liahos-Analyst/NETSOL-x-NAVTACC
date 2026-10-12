# Week 1 | Class 03: Conditions and loops
# References from the course document:
# https://www.geeksforgeeks.org/python-for-loops/
# https://www.geeksforgeeks.org/python-while-loops/
# https://www.geeksforgeeks.org/python-break-statement/
# https://www.geeksforgeeks.org/python-continue-statement/
# https://www.geeksforgeeks.org/looping-techniques-python/

marks = [88, 42, 76, 59, 95, 33]

for mark in marks:
    if mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    else:
        grade = "Needs improvement"
    print(f"{mark}: {grade}")

print("\nEven numbers from 1 to 20:")
for number in range(1, 21):
    if number % 2 != 0:
        continue
    print(number, end=" ")
print()

print("\nMultiplication table:")
number = int(input("Choose a number: "))
for multiplier in range(1, 11):
    print(f"{number} x {multiplier} = {number * multiplier}")

# while loop and break
attempts = 0
while attempts < 3:
    answer = input("\nType 'python' to finish: ").strip().lower()
    if answer == "python":
        print("Correct!")
        break
    attempts += 1
else:
    print("Maximum attempts reached.")

# List comprehension
squares = [n * n for n in range(1, 6)]
print("Squares:", squares)
