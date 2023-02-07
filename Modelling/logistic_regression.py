#this file tries to implement simple logistic regression. however it gives poor results.
#implementation of confusion matrix is here as well. 

from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def logreg():
    with open ('Pickles/train_x.ob', 'rb') as fp:
        train_x = pickle.load(fp)
    with open ('Pickles/train_y.ob', 'rb') as fp:
        train_y = pickle.load(fp)   
    with open ('Pickles/test_x.ob', 'rb') as fp:
        test_x = pickle.load(fp)    
    with open ('Pickles/test_y.ob', 'rb') as fp:
        test_y = pickle.load(fp)
    
    logreg = LogisticRegression(max_iter = 10000)

    train_x, train_y = flatten(train_x, train_y)
    test_x, test_y = flatten(test_x, test_y)

    logreg.fit(train_x, train_y)

    y_pred = logreg.predict(test_x)

    cnf_matrix = metrics.confusion_matrix(test_y, y_pred)

    print("Accuracy: ", metrics.accuracy_score(test_y, y_pred))
    print("Precision: ", metrics.precision_score(test_y, y_pred))
    print("Recall: ", metrics.recall_score(test_y, y_pred))
    print("F1: ", metrics.f1_score(test_y, y_pred))

    visualize_matrix(cnf_matrix)
    print (cnf_matrix)

    # cnf_matrix = [[122, 15], [6,7]]
    visualize_matrix(cnf_matrix)


def flatten(train_x, train_y):
    train_x = np.array(train_x)

    train_x = np.reshape(train_x, (len(train_x), 15000))
    
    train_y = np.array(train_y)

    train_y = np.reshape(train_y, (len(train_y)))

    # print(len(train_x))
    # print(len(train_y))
    
    return train_x, train_y

def visualize_matrix(matrix):
    class_names = ["NonStutter", "Stutter"]
    fig,ax = plt.subplots()
    tick_marks = np.arange(len(class_names))
    plt.xticks(tick_marks, class_names)
    plt.yticks(tick_marks, class_names)

    sns.heatmap(pd.DataFrame(matrix), annot=True, cmap="YlGnBu", fmt='g')
    # ax.xaxis.set_label_position("top")
    # plt.tight_layout()
    plt.title("Confusion matrix", y=1.1)
    plt.ylabel("Actual Label")
    plt.xlabel("Predicted Label")
    ax.xaxis.set_ticklabels(["No Stutter", "Stutter"])
    ax.yaxis.set_ticklabels(["No Stutter", "Stutter"])
    plt.show()

if __name__ == "__main__":
    logreg()    