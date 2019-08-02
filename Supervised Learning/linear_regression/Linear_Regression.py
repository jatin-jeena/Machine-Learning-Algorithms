# importing the necessary librairies.
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# reading the dataset "Housing.csv" using pandas and also printing it.
data = pd.read_csv('Housing.csv')
print(data)

# Splitting the data into training and testing data in the ratio 70:30.
x_train, x_test, y_train, y_test = train_test_split(data['lotsize'], data['price'],  test_size=0.3,
                                                    random_state=1)
# reshapping the training data into required format.
x_train = np.array(x_train)
y_train = np.array(y_train)
x_train = x_train.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)

# Training the model with training data.
clf = LinearRegression()
clf.fit(x_train, y_train)

x_test = np.array(x_test)
x_test = x_test.reshape(-1, 1)

# Using the model to predict the prices for testing data.
predic = clf.predict(x_test)

# Printing the predicted Prices.
print("The predicted values are :", predic)

