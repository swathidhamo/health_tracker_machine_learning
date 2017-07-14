import numpy as np
import csv 
import math
import operator
import random

def load(filename,x_parameters=[],y_parameters = [],x_test = [],y_test = []):
    with open(filename,'rb') as csvfile:
        lines = csv.reader(csvfile)
        data = list(lines)
        for x in range(len(data)-1):
            for y in range(2):
                data[x][y] = int(data[x][y])
                

            if random.random() < 0.80:

                x_parameters.append(data[x][0])
                y_parameters.append(data[x][-1]) 

            else:
                x_test.append(data[x][0])
                y_test.append(data[x][-1])


                

           
def writeData(filename,data):
    data_send = csv.writer(open(filename,"wb"))
    data_send.writerow(["name","address",data])

            




            
                

def predictTimePeriod(a,b,x_parameter):
    y_parameter = (a*x_parameter)+b
    answer = int(round(y_parameter))
    return answer
def getAccuracy(y_predictions,y_test):
    correct = 0
    for j in range(len(y_predictions)):
        if y_predictions[j] >= y_test[j]:
            correct += 1
          
        
    return correct






def main():
    x_parameters = []
    y_parameters = []
    x_test = []
    y_test = []
    y_prediction = []
    

    load('medicine.data',x_parameters,y_parameters,x_test,y_test)
    b = np.array(y_parameters)
    n = len(x_parameters)
    a=np.array(([[x_parameters[j], 1] for j in range(n)]))
    x = np.linalg.lstsq(a,b)[0]
    answer_a = x[0]
    answer_b = x[1]
    

    for i in range((len(x_test)-1)):
        prediction = predictTimePeriod(answer_a,answer_b,x_test[i])
        y_prediction.append(prediction)
        print prediction,"this is the actual value",y_test[i]

    
      

    

    #a = np.array(([[x_parameters[j],1] for j in range(n)])


    #A = np.vstack([x_parameters, np.ones(len(x_parameters))]).T

    #m, c = np.linalg.lstsq(A, y_parameters)[0]
    #print A
    y_value = 9
    
    print "Line is y = ",answer_a,"x+",answer_b
    result = predictTimePeriod(answer_a,answer_b,y_value)
    print "This is the result for lest symptoms",result
    writeData("getData.csv",result)





'''
y = [-6,-5,-10,-5,-8,-3,-6,-8,-8]
x = [[-4.95,-4.55,-10.96,-1.08,-6.52,-0.81,-7.01,-4.46,-11.54],[-5.87,-4.52,-11.64,-3.36,-7.45,-2.36,-7.33,-7.65,-10.03],[-0.76,-0.71,-0.98,0.75,-0.86,-0.50,-0.33,-0.94,-1.03],[14.73,13.74,15.49,24.72,16.59,22.44,13.93,11.40,18.18],[4.02,4.47,4.18,4.96,4.29,4.81,4.32,4.43,4.28],[0.20,0.16,0.19,0.16,0.10,0.15,0.21,0.16,0.21],[0.45,0.50,0.53,0.60,0.48,0.53,0.50,0.49,0.55]]
X = np.column_stack(x+[[1]*len(x[0])])
beta_hat = np.linalg.lstsq(X,y)[0]
print beta_hat
'''

main()