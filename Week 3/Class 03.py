# Week 3 | Class 03: NumPy arrays, attributes and operations
# Reference: https://numpy.org/doc/1.24/

import numpy as np

from_list = np.array([10, 20, 30, 40])
zeros = np.zeros((2, 3))
ones = np.ones(4)
sequence = np.arange(0, 10, 2)
random_values = np.random.default_rng(42).integers(1, 100, size=(3, 3))

print("From list:", from_list)
print("Zeros:\n", zeros)
print("Ones:", ones)
print("Sequence:", sequence)
print("Random matrix:\n", random_values)

print("\nAttributes:")
print("shape:", random_values.shape)
print("ndim:", random_values.ndim)
print("size:", random_values.size)
print("dtype:", random_values.dtype)
print("max/min:", random_values.max(), random_values.min())
print("argmax:", random_values.argmax())

print("\nArithmetic:")
print(from_list + 5)
print(from_list * 2)
print(np.sqrt(from_list))
print("Mean:", from_list.mean())

print("\nReshape:", np.arange(12).reshape(3, 4))
print("Concatenate:", np.concatenate([from_list, [50, 60]]))
print("Split:", np.array_split(np.arange(10), 3))
