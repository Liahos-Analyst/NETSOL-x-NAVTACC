# Week 2 | Class 04: Descriptive statistics and probability basics
# Course reference tasks:
# https://www.w3schools.com/python/python_ml_mean_median_mode.asp
# https://www.w3schools.com/python/python_ml_standard_deviation.asp

import statistics
import random

scores = [65, 70, 70, 75, 82, 90, 98]
mean_value = statistics.mean(scores)
median_value = statistics.median(scores)
mode_value = statistics.mode(scores)
variance_value = statistics.variance(scores)
stdev_value = statistics.stdev(scores)

print("Scores:", scores)
print("Mean:", round(mean_value, 2))
print("Median:", median_value)
print("Mode:", mode_value)
print("Sample variance:", round(variance_value, 2))
print("Sample standard deviation:", round(stdev_value, 2))
print("Range:", max(scores) - min(scores))
print("Coefficient of variation (%):", round(stdev_value / mean_value * 100, 2))

# Simple empirical probability
random.seed(7)
rolls = [random.randint(1, 6) for _ in range(1000)]
prob_six = rolls.count(6) / len(rolls)
print("\nEstimated probability of rolling a six:", round(prob_six, 3))

# Z-score for one observation
observation = 90
z_score = (observation - mean_value) / stdev_value
print("Z-score for 90:", round(z_score, 2))
