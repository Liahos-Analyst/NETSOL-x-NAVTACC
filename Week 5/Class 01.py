# Week 5 | Class 01: Multivariate linear regression

import numpy as np

# Predict house price using area and number of bedrooms.
X = np.array([
    [700, 1], [850, 2], [1000, 2], [1200, 3], [1500, 3],
    [1800, 4], [2000, 4], [2300, 4], [2500, 5], [2800, 5]
], dtype=float)
y = np.array([35, 42, 48, 58, 68, 78, 85, 95, 105, 115], dtype=float)

try:
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_absolute_error, r2_score

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print("Feature coefficients [area, bedrooms]:", model.coef_)
    print("Intercept:", model.intercept_)
    print("Actual:", y_test)
    print("Predicted:", np.round(pred, 2))
    print("MAE:", round(mean_absolute_error(y_test, pred), 2))
    print("R2:", round(r2_score(y_test, pred), 3))
    print("Estimate for 1600 sqft, 3 bedrooms:", round(model.predict([[1600, 3]])[0], 2))
except ImportError:
    print("Install required package: pip install scikit-learn")
