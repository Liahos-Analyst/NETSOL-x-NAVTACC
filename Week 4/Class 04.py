# Week 4 | Class 04: Machine-learning workflow and simple linear regression
# Reference listed in the course PDF:
# https://stackabuse.com/linear-regression-in-python-with-scikit-learn/

import numpy as np

# Predict exam score from study hours using a simple baseline model.
X = np.array([1, 2, 3, 4, 5, 6], dtype=float).reshape(-1, 1)
y = np.array([48, 52, 60, 65, 71, 79], dtype=float)

try:
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=42
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Intercept:", round(model.intercept_, 3))
    print("Coefficient:", round(model.coef_[0], 3))
    print("Actual:", y_test)
    print("Predicted:", np.round(predictions, 2))
    print("MAE:", round(mean_absolute_error(y_test, predictions), 3))
    print("MSE:", round(mean_squared_error(y_test, predictions), 3))
    print("RMSE:", round(np.sqrt(mean_squared_error(y_test, predictions)), 3))
    print("R2:", round(r2_score(y_test, predictions), 3))
    print("Predicted score for 7 study hours:", round(model.predict([[7]])[0], 2))
except ImportError:
    print("Install required package: pip install scikit-learn")
    # Simple least-squares calculation without scikit-learn
    slope, intercept = np.polyfit(X.ravel(), y, 1)
    print("Slope:", slope, "Intercept:", intercept)
    print("Prediction for 7 hours:", slope * 7 + intercept)
