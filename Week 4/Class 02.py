# Week 4 | Class 02: Pandas groupby, merge, binning and plots

import pandas as pd

students = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "name": ["Ali", "Sara", "Hamza", "Mina", "Noor"],
    "score": [65, 91, 72, 48, 85],
    "department": ["AI", "DS", "AI", "DS", "AI"],
})
attendance = pd.DataFrame({
    "student_id": [1, 2, 3, 5],
    "attendance_pct": [80, 95, 75, 98],
})

merged = students.merge(attendance, on="student_id", how="left")
merged["attendance_pct"] = merged["attendance_pct"].fillna(0)
merged["score_band"] = pd.cut(
    merged["score"], bins=[0, 50, 70, 85, 100],
    labels=["Needs work", "Developing", "Good", "Excellent"],
    include_lowest=True
)

print("Merged data:\n", merged)
print("\nDepartment summary:\n", merged.groupby("department")["score"].agg(["mean", "min", "max"]))
print("\nScore band counts:\n", merged["score_band"].value_counts())

# Plotting is optional; script still works without Matplotlib.
try:
    import matplotlib.pyplot as plt
    merged.plot(x="name", y="score", kind="bar", legend=False, title="Student scores")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.savefig("week4_scores.png")
    plt.show()
except ImportError:
    print("Install matplotlib to create the plot: pip install matplotlib")
