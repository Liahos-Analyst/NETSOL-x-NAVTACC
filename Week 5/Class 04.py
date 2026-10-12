# Week 5 | Class 04: Multiclass logistic regression and model practice

import numpy as np

# Three classes of flowers represented by two numeric features.
X = np.array([
    [1.0, 1.2], [1.2, 1.1], [0.8, 1.0], [1.1, 0.9],
    [3.0, 3.2], [3.2, 2.9], [2.8, 3.1], [3.1, 3.0],
    [5.0, 1.0], [5.2, 1.2], [4.8, 0.9], [5.1, 0.8]
])
y = np.array(["Class A"] * 4 + ["Class B"] * 4 + ["Class C"] * 4)

try:
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=1000, random_state=42)
    )
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print("Classes:", model.classes_[1] if hasattr(model, "classes_") else "see model")
    print("Actual:", y_test)
    print("Predicted:", pred)
    print("Accuracy:", round(accuracy_score(y_test, pred), 3))
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred, zero_division=0))
except ImportError:
    print("Install required package: pip install scikit-learn")
