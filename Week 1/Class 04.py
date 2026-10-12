# Week 1 | Class 04: Functions, iterables and file basics
# User-defined functions are also listed here:
# https://www.geeksforgeeks.org/functions-in-python/

def calculate_average(values):
    if not values:
        return 0
    return sum(values) / len(values)

def classify_score(score):
    return "Pass" if score >= 50 else "Try again"

scores = [65, 81, 44, 90]
print("Average:", calculate_average(scores))
for score in scores:
    print(score, classify_score(score))

# enumerate and zip
names = ["Ali", "Sara", "Hamza"]
for index, name in enumerate(names, start=1):
    print(index, name)

subjects = ["Python", "Statistics", "AI"]
for name, subject in zip(names, subjects):
    print(f"{name} is studying {subject}")

# Write and read a small text file
filename = "week1_notes.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write("Python basics completed.\n")
    file.write("Next: functions and data analysis.\n")

with open(filename, "r", encoding="utf-8") as file:
    print("\nFile contents:\n" + file.read())
