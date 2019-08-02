# importing the necessary libraries.
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# importing the load_breast_cancer dataset from sklearn inbuilt datasets.
from sklearn.datasets import load_breast_cancer


bs = load_breast_cancer()
x = bs.feature_names

# printing the feature names.
print(x)
y = bs.target_names

# printing the label/target names. we have two labels, two types of cancers - 'malignant','benign'.
print(y)

# splitting the dataset into training and testing data. testing data is 30% of the dataset and
# training data is 70% of the  dataset.
x_train, x_test,  y_train, y_test = train_test_split(bs.data, bs.target, test_size=0.3, random_state=1)
clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=50)

# Training the model from training data.
clf.fit(x_train, y_train)

# using the model to predict the labels for testing data.
predic = clf.predict(x_test)

# Finding the accuracy. Accuracy is found to be 84.795.
print("Accuracy using Decision Tree ", accuracy_score(y_test, predic)*100)
