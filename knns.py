
# Example of kNN implemented from Scratch in Python
 
import csv
import random
import math
import operator
 #this is a sample record 5.2 3.4, 1.4  0.2 Iris-setosa
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(10):
	        	dataset[x][y] = int(dataset[x][y])
	        		

	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])

def euclidean(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow(instance1[x]-instance2[x], 2)
	return math.sqrt(distance)	

def getNeighbors(trainingSet,testInstance, k):
	#here you give the set it trains from each time it is given an instance to predict
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclidean(testInstance,trainingSet[x],length)
		distances.append((trainingSet[x],dist))
	distances.sort(key=operator.itemgetter(1))#sort the list based on distances
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])#capture the first 'k' neighbours
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	#create an object called class votes that will record number of votes
	for x in range(len(neighbors)):
		response = neighbors[x][-1]#check to see if the last  neighbour is common
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(),key=operator.itemgetter(1),reverse=True)#to flag a descending sort 
	return sortedVotes[0][0]

def getAccuracy(testSet,predictions):
	correct = 0
	for x in range(len(testSet)):
	
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0		

	
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	split = 0.87
	loadDataset('cancer.data', split, trainingSet, testSet)
	print 'Train set: ' + repr(len(trainingSet))
	print 'Test set: ' + repr(len(testSet))

	#generate predictions

	predictions = []
	k = 5
	for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet,testSet[x],k)
		result = getResponse(neighbors)
		predictions.append(result)
		print('>preducted='+repr(result)+', actual=' + repr(testSet[x][-1]))

	accuracy = getAccuracy(testSet,predictions)
	print('Accuracy FOR THE PROJECT: ' + repr(accuracy) + '%')	

	
	
main()