import numpy as np
import csv 
import math
import operator
import random
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt 


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
    

    load('regr.csv',x_parameters,y_parameters,x_test,y_test)
    b = np.array(y_parameters)
    n = len(x_parameters)
    n_y = len(y_parameters)
    c = np.array(x_parameters)
    intercept = stats.linregress(c,b)
    answer_a = intercept[0]
    answer_b = intercept[1]
    reg_line = [(answer_a*x + answer_b) for x in c]
    plt.scatter(c,b,color = "red")
    plt.plot(c,reg_line)
    plt.ylabel("medicine time")
    plt.xlabel("medicine effect")
    plt.show()
    
    print "Scipy intercept ",intercept[0], "       ",intercept

    '''
    a=np.array(([[x_parameters[j], 1] for j in range(n)]))
    x = np.linalg.lstsq(a,b)[0]
    answer_a = x[0]
    answer_b = x[1]
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




main()