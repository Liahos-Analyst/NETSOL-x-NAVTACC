# Week 6 | Class 04: Decision tree, SVM and time-series introduction
# Course references:
# Decision tree: https://www.datacamp.com/community/tutorials/decision-tree-classification-python
# SVM: https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/
# Time series: https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas

import numpy as np
import pandas as pd

try:
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score, classification_report

    # Small binary-classification dataset
    X = np.array([
        [1, 20], [2, 22], [2, 25], [3, 28], [4, 35], [5, 40],
        [6, 45], [7, 50], [8, 55], [9, 60], [10, 65], [10, 70]
    ], dtype=float)
    y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    for name, model in [
        ("Decision Tree", DecisionTreeClassifier(max_depth=3, random_state=42)),
        ("SVM", SVC(kernel="linear"))
    ]:
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        print(f"\n{name} accuracy:", round(accuracy_score(y_test, pred), 3))
        print(classification_report(y_test, pred, zero_division=0))
except ImportError:
    print("Install scikit-learn: pip install scikit-learn")

# Time series: monthly values, trend and rolling average
dates = pd.date_range("2025-01-01", periods=12, freq="MS")
sales = pd.Series([120, 128, 125, 140, 145, 151, 160, 158, 170, 178, 182, 195], index=dates)
ts = pd.DataFrame({"sales": sales})
ts["monthly_change"] = ts["sales"].diff()
ts["rolling_mean_3"] = ts["sales"].rolling(3).mean()
print("\nTime series:\n", ts)
print("\nResampled quarterly mean:\n", ts["sales"].resample("QS").mean())
