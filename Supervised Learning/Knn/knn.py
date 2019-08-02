from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def naive(inputs, outputs):
    xtrain, xtest, ytrain, ytest = train_test_split(inputs, outputs, random_state=47, test_size=0.15)
    clf = KNeighborsClassifier(k_neighbors=10)
    clf.fit(xtrain, ytrain)
    ans = clf.predict(xtest)
    return accuracy_score(y_true=ytest, y_pred=ans) * 100
