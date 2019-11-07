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


class DecisionStump:
    def __init__(self, trainingData):
        self.threshold = 0
        self.splitValue = 0
      	self.trainingData = trainingData


	def setSplit(self):
    #returns a float value that divides the two splits with the highest.  
	############################################################################
    # FILL THIS IN
    ############################################################################
       
        
        return self.splitValue



    def classify(dataPoint):
    #returns an int value 0 or 1 denoting flu or cold if you input a single datapoint
    ############################################################################
    # FILL THIS IN
    ############################################################################

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
# accurate the decision tree is on the test data.  Please use this to test how accurate you are.
def testDecisionStump(trainingData, testData):
    numCorrect = 0
    stump = DecisionStump(trainingData)
    splitValue = DecisionStump.setSplit()

    for i in range(len(testData)):
        label = DecisionStump.classify(testData[i][0])
        if label == testData[i][1]:
            numCorrect +=1
    
    return float(numCorrect)/float(len(testData))






  

























			









