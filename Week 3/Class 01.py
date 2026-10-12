# Week 3 | Class 01: Correlation, percentiles, skew and kurtosis

import statistics
try:
    import numpy as np
except ImportError:
    np = None

study_hours = [1, 2, 2, 3, 4, 5, 6]
scores = [48, 53, 57, 61, 70, 78, 89]

def pearson_correlation(x, y):
    mean_x, mean_y = statistics.mean(x), statistics.mean(y)
    numerator = sum((a - mean_x) * (b - mean_y) for a, b in zip(x, y))
    denominator = (sum((a - mean_x) ** 2 for a in x) *
                   sum((b - mean_y) ** 2 for b in y)) ** 0.5
    return numerator / denominator if denominator else 0

print("Correlation (study hours vs score):", round(pearson_correlation(study_hours, scores), 3))
print("Quartiles (manual median-based view):")
ordered = sorted(scores)
print("Min:", min(ordered), "Median:", statistics.median(ordered), "Max:", max(ordered))

if np is not None:
    arr = np.array(scores, dtype=float)
    print("25th, 50th, 75th percentiles:", np.percentile(arr, [25, 50, 75]))
    print("Variance:", np.var(arr), "Std:", np.std(arr))
else:
    print("Install NumPy for percentile and array statistics: pip install numpy")

# Relationship does not automatically mean causation.
print("\nInterpretation: correlation describes association, not proof of causation.")
