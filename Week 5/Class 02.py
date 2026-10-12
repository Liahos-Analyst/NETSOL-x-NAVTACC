# Week 5 | Class 02: Polynomial regression

import numpy as np

# Example: relationship that curves rather than following a straight line.
X = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float).reshape(-1, 1)
y = np.array([3, 6, 11, 18, 27, 38, 51, 66], dtype=float)

try:
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error

    model = make_pipeline(PolynomialFeatures(degree=2, include_bias=False), LinearRegression())
    model.fit(X, y)
    predictions = model.predict(X)

    print("Input | Actual | Predicted")
    for x, actual, pred in zip(X.ravel(), y, predictions):
        print(f"{x:>5.1f} | {actual:>6.1f} | {pred:>9.2f}")
    print("Training RMSE:", round(np.sqrt(mean_squared_error(y, predictions)), 3))
    print("Prediction at x=9:", round(model.predict([[9]])[0], 2))
except ImportError:
    print("Install required package: pip install scikit-learn")
