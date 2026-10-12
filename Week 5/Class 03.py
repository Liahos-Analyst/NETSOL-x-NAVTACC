# Week 5 | Class 03: Logistic regression for binary classification
# Course reference:
# https://www.datacamp.com/community/tutorials/understanding-logistic-regression-python

import numpy as np

# Predict whether a student passes based on study hours and attendance.
X = np.array([
    [1, 50], [2, 55], [2, 60], [3, 60], [3, 70], [4, 65],
    [4, 75], [5, 70], [5, 85], [6, 80], [7, 90], [8, 95]
], dtype=float)
y = np.array([0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1])

try:
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = make_pipeline(StandardScaler(), LogisticRegression(random_state=42))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print("Predicted labels:", pred)
    print("Actual labels:   ", y_test)
    print("Accuracy:", round(accuracy_score(y_test, pred), 3))
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred, zero_division=0))
    print("Pass probability for 5 study hours and 80% attendance:",
          round(model.predict_proba([[5, 80]])[0, 1], 3))
except ImportError:
    print("Install required package: pip install scikit-learn")
