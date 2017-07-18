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
	
	





main()
