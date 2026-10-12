# Week 3 | Class 04: NumPy indexing, slicing, filtering and saving

import numpy as np

data = np.arange(1, 13).reshape(3, 4)
print("Array:\n", data)
print("First row:", data[0])
print("Element row 2, col 3:", data[1, 2])
print("First two rows, last two columns:\n", data[:2, 2:])
print("Values greater than 6:", data[data > 6])

# Copy versus view
view = data[:, :2]
copy = data[:, :2].copy()
view[0, 0] = 999
print("\nOriginal after changing view:\n", data)
copy[0, 0] = -1
print("Copy changed independently:\n", copy)

# Broadcasting and type casting
temperatures = np.array([20, 22, 25], dtype=float)
print("Fahrenheit:", temperatures * 9 / 5 + 32)
integer_temperatures = temperatures.astype(int)
print("Integer values:", integer_temperatures)

# Save and load arrays
np.save("week3_array.npy", data)
loaded = np.load("week3_array.npy")
print("Loaded array matches:", np.array_equal(data, loaded))
