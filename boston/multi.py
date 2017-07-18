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

		
				value = len(data[x])-2
					
			
				li.append(float(data[x][y]))
			    
		

		   # li.append(value)
			x_parameters.append(li)  
			if data[x]:
				y_parameters.append(float(data[x][-1]))
			#y_parameters.append(float(data[x][len(data[x])-1]))

			 
					
				   
				
def findNoise(filename,noise = []):
	with open(filename,'rb') as csvfile:
		lines_noise = csv.reader(csvfile)
		data = list(lines_noise)
		max_value = 0
		#print noise
		counter = 0
		for x in range(len(data)-2):
			noise.append(len(data[x]))
			if x%100==0:
				print noise

		  



				






		   
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
	noise = []
	y_parameter = []
	#findNoise("Boston_Housing.csv",noise)
	#print noise

	#with respect to the fit fuction what we try to do is just make it find out the linear coefficients that can 
	#in turn do somethinng to predict more values like that
	#but my entire flask and implementait

	load('Boston_Housing.csv',x_parameters,y_parameters,x_test,y_test)
	
	x_parameter = np.matrix(x_parameters)
	#y_parameters = np.array(y_parameters)
	print y_parameters

	#y_parameter = np.reshape(y_parameters,(1,-1))
	y_parameter= np.array(y_parameters)
	y_parameter = np.reshape(y_parameter,(1,-1))

	print y_parameter.ndim
	#y_parameter = np.array(y_parameters)[:,None]
	#y_parameter = np.atleast_2d(y_parameters).T
	
	y_paramete = np.matrix(y_parameter)
	reg = linear_model.LinearRegression();
	reg.fit(x_parameters,y_parameter)
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
	#print x_parameters,"      ",y_parameters      


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