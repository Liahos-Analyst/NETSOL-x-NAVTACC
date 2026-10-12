# Week 1 | Class 02: Lists, tuples, dictionaries and sets
# Reference links in the course document:
# https://www.programiz.com/python-programming/list
# https://www.programiz.com/python-programming/tuple
# https://www.programiz.com/python-programming/string
# https://www.programiz.com/python-programming/set
# https://www.programiz.com/python-programming/dictionary

# Lists: ordered and changeable
scores = [78, 92, 85, 92, 67]
scores.append(88)
scores[0] = 80
print("Scores:", scores)
print("First two:", scores[:2])
print("Sorted:", sorted(scores))
print("Highest:", max(scores), "| Average:", sum(scores) / len(scores))

# Tuples: ordered and immutable
student = ("Ayesha", "Data Science", 1)
print("\nTuple:", student)
print("Student name:", student[0])

# Dictionaries: key-value pairs
profile = {"name": "Ayesha", "course": "AI", "completed": False}
profile["completed"] = True
profile["score"] = 91
print("\nProfile:", profile)
print("Keys:", list(profile.keys()))
print("Values:", list(profile.values()))

# Sets: unique values
topics = {"Python", "AI", "Python", "ML"}
topics.add("NLP")
print("\nUnique topics:", topics)

# Practical mini-task: simple shopping basket
basket = {"apples": 3, "milk": 1, "bread": 2}
prices = {"apples": 50, "milk": 220, "bread": 120}
total = sum(prices[item] * qty for item, qty in basket.items())
print("Basket:", basket)
print("Total bill:", total)
