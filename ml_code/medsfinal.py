
# Example of kNN implemented from Scratch in Python
 
import csv
import random
import math
import operator
 
def dataset(filename, split, training=[] , test=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            training.append(dataset[x])
	        else:
	            test.append(dataset[x])
 
 
def euclideanDistance(l1, l2, length):
	distance = 0
	for x in range(length):
		distance += pow((l1[x] - l2[x]), 2)
	return math.sqrt(distance)
 
def neighbors(trainingSet, test, k):
	lengths = []
	length = len(test)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(test, trainingSet[x], length)
		lengths.append((trainingSet[x], dist))
	lengths.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(lengths[x][0])
	return neighbors
 
def response(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]
 
def accuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]-1:
			correct+= 1
		
	return (correct/float(len(testSet))) * 100.0
	
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	split = 0.80
	dataset('meds_four.csv', split, trainingSet, testSet)
	print 'Train ' + repr(len(trainingSet))
	print 'Test ' + repr(len(testSet))
	# generate predictions
	predictions=[]
	k = 3
	for x in range(len(testSet)):
		neighbors = neighbors(trainingSet, testSet[x], k)
		predicted_result = response(neighbors)
		predictions.append(predicted_result)
		print('> predicted=' + repr(predicted_result) + ', actual=' + repr(testSet[x][-1]))
	accuracy = accuracy(testSet, predictions)
	print('Accuracy: ' + repr(accuracy) + '%')
	
main()