# stuff to run always here such as class/def

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def predict(a, b, c, d):

    x_new = pd.DataFrame(
        {'is_family_friendly': [a],
            'session_count': [b], 'level': [c], 'risk': [d]}
    )

    new_pred = logreg.predict(x_new)
    new_pred_labels = np.argmax(new_pred, axis=0)

    #import numpy as np

    # Define a dictionary that maps numbers to words
    num_to_word = {
        0: "eligible",
        1: "rejected"
    }

    if new_pred_labels in num_to_word:
        print(num_to_word[new_pred_labels])



if __name__ == "__main__":
    #logisic regression

    app = pd.read_csv('ressources/applicants.csv')
    ins = app["account_id"].dtype

    feature_cols = ['is_family_friendly', 'session_count','level','risk']
    X = app[feature_cols] # Features
    y = app.response # Target variable

    # split X and y into training and testing sets
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=16)

    #modelling
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

    # instantiate the model (using the default parameters)
    logreg = LogisticRegression(random_state=16)

    # fit the model with data
    logreg.fit(X_train, y_train)

    y_pred = logreg.predict(X_test)


    # import the metrics class
    from sklearn import metrics

    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)

    disp = ConfusionMatrixDisplay(cnf_matrix)
    #disp.plot()

    plt.show()

    from sklearn.metrics import classification_report
    target_names = ['Eligible', 'Rejected']
    print(classification_report(y_test, y_pred, target_names=target_names))
    # stuff only to run when not called via 'import' here
    predict()
   
   
   