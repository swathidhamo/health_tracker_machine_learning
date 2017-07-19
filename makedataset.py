import math
import random 


def inRange(y_prediction,y_value):

	difference = y_prediction-y_value
	difference = abs(difference)
	error_range = 0.12
	error = difference/y_value
	if error>error_range:
		return True
	else:
		return False

def constraintValues(random_num,length,y,error_value,data=[]):


	for x in range(length-1):
		difference = data[x][y]-random_num
		difference = abs(difference)
		difference = difference/data[x][y]
		if difference >= error_value:
			return True
		else:
			return False






def main():
	rows = 10
	data = []
	error_values = []
	y_parameter = []
	range_lower = [0,0,0,10,40,100]
	range_upper = [10,10,10,70,200,240]
	'''for k in range(len(range_upper)-1):
		value = range_upper[k]-range_lower[k]
		value = value/range_upper
		error_values.append(value)'''
	error_range = 0.12

	#s_one,s_two,s_three,age,weight,height
	





	
	for x in range(10):
		single_row = []
		y_value = random.randint(7,23)
		y_parameter.append(y_value)
		index = 0
		match_value = False
		#to check if the y_value is close to a preset constraint
		while(index<len(y_parameter)and match_value==False):


			if inRange(y_value,y_parameter[index]):
				match_value = True
			else:
				match_value = False
				index = index + 1

		for y in range(5):
			random_data = random.randint(range_lower[y],range_upper[y])

			if match_value:
				while(constraintValues(random_data,x,y,error_range,data)==True):
					random_data = random.randint(range_lower[y],range_upper[y])

				single_row.append(random_data)
	data.append(single_row)
	print data, "       ",y_parameter

'''



			if y==0:
				random_0 = random.randint(0,10)
				single_row.append(random_0)
			if y==1:
				random_1 = random.randint(0,10)
				single_row.append(random_1)
			if y==2:
				random_2 = random.randint(0,10)
				single_row.append(random_2)
			if y==3:
				random_3 = random.randint(10,40)
				single_row.append(random_3)
			if y==4:
				random_4 = random.randint(40,200)
				single_row.append(random_4)
			else:
				random_5 = random.randint(100,240)


				single_row.append(random_5)

		data.append(single_row)'''
	#print data,"             ",y_parameter










			

main()
