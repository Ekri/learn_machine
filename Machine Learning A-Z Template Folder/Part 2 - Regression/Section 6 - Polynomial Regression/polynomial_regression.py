# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# from sklearn.model_selection import train_test_split
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)



from sklearn.linear_model import LinearRegression

linear_regressor = LinearRegression()
linear_regressor.fit(X, y)

# # Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures

polynomial_regression = PolynomialFeatures(degree=4)
X_polynomial = polynomial_regression.fit_transform(X)
linear_regressor_2 = LinearRegression()
linear_regressor_2.fit(X_polynomial, y)

# # Visualising the Linear Regression results
plt.scatter(X, y, color='red')
plt.plot(X, linear_regressor.predict(X), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
# plt.show()

# # Visualising the Polynomial Regression results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))

plt.scatter(X, y, color='red')
plt.plot(X_grid, linear_regressor_2.predict(polynomial_regression.fit_transform(X_grid)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
# plt.show()

# # Predicting a new result with Linear Regression
print linear_regressor.predict(6.5)

# # Predicting a new result with Polynomial Regression
print linear_regressor_2.predict(polynomial_regression.fit_transform(6.5))

