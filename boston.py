import numpy as np
import csv 
import math
import operator
import random
from scipy import stats
from sklearn import datasets, linear_model, metrics
from sklearn import mean_squared_error

def load(filename,x_parameters=[],y_parameters = [],x_test = [],y_test = [],split):
    
    with open(filename,'rb') as csvfile:
        lines = csv.reader(csvfile)
        data = list(lines)
        value = 1
        for x in range(len(data)-60):
            li = []
            for y in range(len(data[x])-1):
            
            if random.random()<split:
                if y!=(len(data[x])-1):
                    li.append(float(data[x][y]))
            y_parameters.append(float(data[x][-1]))
            x_parameters.append(li)   
            li = []     
            else:
                if y!=(len(data[x])-1):
                    li.append(float(data[x][y]))
            y_test.append(float(data[x][-1]))
            x_test.append(li)        


           
def writeData(filename,data):
    data_send = csv.writer(open(filename,"wb"))
    data_send.writerow([data])

def checkAccuracy(y_prediction,y_test):
    counter = 0
    if len(y_prediction)!=len(y_test):
        print "Cannot check for unequal values"
    else:
        for x in range(len(y_prediction)-1):
            if y_prediction[x] == y_test[x]:
                counter = counter+1
    counter = counter /(len(y_prediction))
    counter = counter*100            
    return counter            
def meanSquareError(y_prediction,y_test):
    sum_error = 0
    length = len(y_prediction)
    for x in range(length-1):
        difference  = y_prediction[x]-y_test[x]
        sum_error+= math.pow(difference,2)
    meanSquare = sum_error/length
    return meanSquare



def main():
    x_parameters = []
    y_parameters = []
    x_test = []
    y_test = []
    y_prediction = []



    load('medicine.csv',x_parameters,y_parameters,x_test,y_test)
    x_parameters.pop(0)
    x_test.pop(0)
    x_parameter = np.matrix(x_parameters)
    y_parameter = np.matrix(y_parameters)
    reg = linear_model.LinearRegression();
    reg.fit(x_parameters,y_parameters)
    predictionData = np.array(x_test)
    y_prediction = reg.predict(predictionData)
    accuracy = checkAccuracy(y_prediction,y_test)
    print "The accuracy of this model is ", accuracy, " %. "




    print "Coefficinets", reg.coef_

main()