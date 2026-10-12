# Week 4 | Class 03: Seaborn visualization and exploratory data analysis

import pandas as pd

df = pd.DataFrame({
    "age": [19, 21, 22, 24, 27, 29, 31, 35, 38, 42],
    "study_hours": [1, 2, 3, 3, 4, 5, 5, 6, 7, 8],
    "score": [45, 50, 58, 62, 66, 73, 78, 81, 89, 94],
    "group": ["A", "A", "B", "B", "A", "B", "A", "B", "A", "B"],
})
print(df.describe())
print("\nCorrelation matrix:\n", df[["age", "study_hours", "score"]].corr())

try:
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set_theme()
    sns.histplot(data=df, x="score", kde=True)
    plt.title("Distribution of scores")
    plt.tight_layout()
    plt.savefig("week4_score_distribution.png")
    plt.show()

    sns.scatterplot(data=df, x="study_hours", y="score", hue="group")
    plt.title("Study hours and score")
    plt.tight_layout()
    plt.savefig("week4_hours_vs_score.png")
    plt.show()

    sns.heatmap(df[["age", "study_hours", "score"]].corr(), annot=True, vmin=-1, vmax=1)
    plt.title("Correlation heatmap")
    plt.tight_layout()
    plt.savefig("week4_correlation.png")
    plt.show()
except ImportError:
    print("Install plotting libraries: pip install seaborn matplotlib")
