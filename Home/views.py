from django.shortcuts import render, HttpResponse

#Importing Machine learning libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Create your views here.
#Home Page 
def index(request):
    return render(request, 'index.html')

#Prediction page 
def predict(request):
    return render(request, 'predict.html')

def result(request):
    path = r"student_info.csv"
    df = pd.read_csv(path)
    df.mean()
    df2 = df.fillna(df.mean())
    df2.isnull().sum()
    X = df2.drop("student_marks", axis = "columns")
    y = df2.drop("study_hours", axis = "columns")
    
    #we use 80% for training and 20% for testing 
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test =train_test_split(X,y, test_size =0.2, random_state = 51)  
    
    # Logic behind linear regression  y = m*x + c
    from sklearn.linear_model import LinearRegression
    lr =LinearRegression()
    lr.fit(X_train,y_train)
    
    #Getting the value input by the user 
    var1 = float(request.GET['n1'])
    
    #predicted value is stored in pred variable
    pred = lr.predict([[var1]])[0][0].round(2)

   # make predictions using the linear regression model
    marks = "The student will obtain " + str(pred) + " % Marks"
    return render(request,'predict.html',{"result":marks})