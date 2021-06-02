import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt


def Prediction(data):

    user_input = pd.DataFrame(data, index =[0])
    
    #import the dataset for training the model
    df = pd.read_csv('heart.csv')
    #Split the data into X = independent values and Y = dependent values 
    x = df.iloc[:,:-1].values
    y = df.iloc[:,-1].values
    #Split the dataset as 75% for traing and 25% for testing
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, random_state=1, test_size= 0.25)
    #feature scaling 
    from sklearn.preprocessing import  StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    #KNN code  k=8 for the best accuracy 
    from sklearn.neighbors import  KNeighborsClassifier
    knn_classifier = KNeighborsClassifier(n_neighbors = 8)
    knn_classifier.fit(X_train, Y_train)
    user_input = sc.transform(user_input)
    p = knn_classifier.predict(user_input)
    
    return p


