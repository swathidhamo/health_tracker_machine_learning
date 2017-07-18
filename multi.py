import numpy as np
import csv 
import math
import operator
import random
from scipy import stats
from sklearn import datasets, linear_model, metrics

def load(filename,x_parameters=[],y_parameters = [],x_test = [],y_test = []):
    
    with open(filename,'rb') as csvfile:
        lines = csv.reader(csvfile)
        data = list(lines)
        value = 1
        for x in range(len(data)-60):
            li = []
            for y in range(len(data[x])-1):
                    
                    if y!=4:
                        li.append(float(data[x][y]))
                    #x_parameters.append(float(data[x][y]))
                    else:
                        x_test.append(float(data[x][y]))
           # li.append(value)
            x_parameters.append(li)  
            y_parameters.append(float(data[x][-1]))          
                   
                

           
def writeData(filename,data):
    data_send = csv.writer(open(filename,"wb"))
    data_send.writerow([data])

            




            
                

def predictTimePeriod(a,b,x_parameter):
    y_parameter = (a*x_parameter)+b
    answer = int(round(y_parameter))
    return answer



def main():
    x_parameters = []
    y_parameters = []
    x_test = []
    y_test = []
    y_prediction = []


    
    '''boston = datasets.load_boston
    X = boston.data
    y = boston.target
    from sklearn.model_selection import train_test_split
    #x_parameters,y_parameters,x_test,y_test = train_test_split(X,y,test_size=0.4,random_state = 1)
'''

    #with respect to the fit fuction what we try to do is just make it find out the linear coefficients that can 
    #in turn do somethinng to predict more values like that
    #but my entire flask and implementait

    load('medicine.csv',x_parameters,y_parameters,x_test,y_test)
    x_parameters.pop(0)
    x_parameter = np.matrix(x_parameters)
    y_parameter = np.matrix(y_parameters)
    reg = linear_model.LinearRegression();
    reg.fit(x_parameters,y_parameters)
    print "Coefficinets", reg.coef_
    '''
    b = np.array(y_parameters)
    n = len(x_parameters)
    c = np.array(x_parameters)
    intercept = stats.linregress(c,b)
    print "Scipy intercept ",intercept[0], "       ",intercept
    answer_a = intercept[0]
    answer_b = intercept[1]


'''
#    a=np.array(([[x_parameters[j], 1] for j in range(n)]))
 #   x = np.linalg.lstsq(c,b)

    #answer_a = x[0]
    #answer_b = x[1]
    print x_parameters,"      ",y_parameters      


'''
    for i in range((len(x_test)-1)):
        prediction = predictTimePeriod(answer_a,answer_b,x_test[i])
        y_prediction.append(prediction)
        print prediction,"this is the actual value",y_test[i]

    

    y_value = 9
    
    print "Line is y = ",answer_a,"x+",answer_b
    result = predictTimePeriod(answer_a,answer_b,y_value)
    print "This is the result for least symptoms",result
    writeData("getData.csv",result)


'''



main()
