import numpy as np
import math
import pickle

################################################################################################
# Predicting Cold or Flu
#
# Various students have had their temperatures taken at the school infirmary.  As the infirmary
# doctor you are trying to figure out if the students have a cold or a flu so you have a better
# idea of what to do next to help them.  
#
# Based on previous student's temperatures and the illness that they had, you can use decision 
# stumps to find what a good dividing point is for a future student's temperature to predict whether
# the student has a cold or flu!
#
#################################################################################################    


# This class represents a single Decision Stump. To create a decision stump,
# do "exampleStump = DecisionStump(data)". The data should be the elements of the training data
# that to train on. 



class DecisionStump(object):
    def __init__(self, trainingData):
        self.threshold = 0
        self.attributeIndex = 0
      	self.trainingData = trainingData
      	self.splitValue = 0
      	self.datapoint = None
    def setSplit(self):		
		bestWeightedImpurity = 1
		currentFraction1 = 0
		currentFraction2 = 0

 
		for i in range(1, len(self.trainingData)):		
			divideLine = i
			zeroCount = 0
			oneCount = 0
			highPoint = 0
			lowPoint = 0

			for firstIndex in range(i):   
				

				if self.trainingData[firstIndex][1] == 0:
					zeroCount +=1

				if self.trainingData[firstIndex][1] == 1:
					oneCount +=1
			#print i
			upFraction = float(oneCount/i)
    		downFraction = float(zeroCount/i)
    		currentFraction1 = 1.0 - ((upFraction)**2.0 + (downFraction)**2.0)
    		print currentFraction1
    		splitWeight1 = i/len(self.trainingData)
    		#print currentFraction1
    		oneCount2 = 0
    		zeroCount2 = 0

    		for secondIndex in range(i, len(self.trainingData)):   
				
				if self.trainingData[secondIndex][1] == 1:
					oneCount2 += 1
				elif self.trainingData[secondIndex][1] == 0:
					zeroCount2 += 1

    		splitWeight2 = (len(self.trainingData)-i)/len(self.trainingData)
    		upFraction2 = float(oneCount2)/(len(self.trainingData)-i)
    		downFraction2 = float(zeroCount2)/(len(self.trainingData)-i)
    		#print upFraction2
    		#print downFraction2
    		#print 1.0 - ((upFraction)**2.0 + (downFraction)**2.0)
    		currentFraction2 = 1.0 - ((upFraction2)**2.0 + (downFraction2)**2.0)

    		weightedImpurity = splitWeight1*currentFraction1 + splitWeight2*currentFraction2
    		#print bestWeightedImpurity
    		if weightedImpurity < bestWeightedImpurity:
    			#print "yo"
    			bestWeightedImpurity = weightedImpurity
    			#print bestWeightedImpurity
    			highPoint = self.trainingData[i][0]
    			#print "highPoint"
    			#print highPoint
    			lowPoint = self.trainingData[i-1][0]
    			#print "lowPoint"
    			#print lowPoint

		self.splitValue = float(highPoint + lowPoint)/2
		return self.splitValue

    def classify(self,dataPoint):
    	self.datapoint = dataPoint

    	if self.datapoint < self.splitValue:
    		return 0
    	else:
    		return 1




    	return label 



# this function takes in a filepath to the stock data, and returns a list of
# 3-tuples representing the data.

def loadDataFromFile(filepath):
	name = str(filepath)
	output = pickle.load(open(name, "rb" ))
	return output



#This function takes in a 2d list and sorts them from the first value in each list within.

def sortByAscendingTemp(data):
    sortedData = sorted(data)
    return sortedData

# this function takes in a decision stump and the test data, and returns how
# accurate the decision tree is on the test data
def testDecisionStump(trainingData, testData):
	numCorrect = 0
	newStump = DecisionStump(trainingData)
	splitValue = newStump.setSplit()
	for i in range(len(testData)):
		label = newStump.classify(testData[i][0])
        if label == testData[i][1]:
            numCorrect +=1
	return float(numCorrect)/float(len(testData))



studentDataPure = loadDataFromFile("studentDataPure.p")
#print studentDataPure

studentTest = loadDataFromFile("studentTest.p")

newStudentData = sortByAscendingTemp(studentDataPure)
print newStudentData

stump = DecisionStump(newStudentData)


x = stump.setSplit()
print x


error = testDecisionStump(newStudentData, studentTest)
print error











			









