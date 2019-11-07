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
def getImpurity(data):
    if len(data) == 0:
        return 0

    numZeros = 0
    for i in range(len(data)):
         if data[i][1] == 0:
             numZeros += 1
    return 1 - (numZeros / len(data))**2 - (1 - (numZeros / len(data)))**2

def getWeightedImpurity(data, possibleSplitIndex):
    leftImpurity = getImpurity(data[:possibleSplitIndex])
    rightImpurity = getImpurity(data[possibleSplitIndex:])
    leftWeight = possibleSplitIndex / len(data)
    rightWeight = 1 - leftWeight
    return leftWeight * leftImpurity + rightWeight * rightImpurity


class DecisionStump:
    """
    This class represents a single Decision Stump. To create a decision stump,
    do "exampleStump = DecisionStump(data)". The data should be the elements of the training data
    to train on. 
    """
    
    def __init__(self, trainingData):
        # |trainingData| is a list of tuples. A tuple in the list is the pair (value, class)
        # where |class| is either 0 or 1.
        # For example, a tuple could be (99.7, 0)
        
        # Initialize class variables
        self.splitValue = 0

        # First, we sort the data. Because the data is a list of tuples, we use a 
        # special way to sort that takes a "lambda function." You don't have to worry
        # about how this works. Now the list is sorted by increasing values (temperatures).
        self.trainingData = sorted(trainingData, key=lambda x: x[0])
    
    def train(self):
        # This function finds the index that divides the two splits with the lowest impurity 
        # It then sets self.splitValue to the mean of the cells to the right and left of the
        # split.

        # Initialize |minImpurity| to the maximum possible value of an impurity
        minImpurity = 1

        # We will update this value with better splits. A "split" is an index in the 
        # list where we split the list into two parts: 1) everything to the left of
        # the index, 2) everything to the right of the index, including the index.
        bestSplitIndex = 0

        for possibleSplitIndex in range(len(self.trainingData)):
            thisImpurity = getWeightedImpurity(self.trainingData, possibleSplitIndex)
            if thisImpurity < minImpurity:
                bestSplitIndex = possibleSplitIndex
                minImpurity = thisImpurity

        if bestSplitIndex == 0:
            self.splitValue = -float('inf')
        elif bestSplitIndex == len(self.trainingData) - 1:
            self.splitValue = float('inf')
        else:
            self.splitValue = (self.trainingData[bestSplitIndex-1][0] 
                    + self.trainingData[bestSplitIndex][0]) / 2

        print("Finished training the decision stump. Our split value is", self.splitValue)

    def classify(self, datapoint):
        #returns an int value 0 or 1 denoting flu or cold if you input a single datapoint
        if datapoint < self.splitValue:
            return 0
        else:
            return 1


####################################################################
# Below this line are utility functions to create the decision stump.
# Feel free to try and understand these if you're curious.
####################################################################

def loadDataFromFile(filepath):
    # This function takes in a filepath to the temperature data, and returns a list of
    # 2-tuples representing the data.
    name = str(filepath)
    output = pickle.load(open(name, "rb" ))
    return output


# this function takes in a decision stump and the test data, and returns how
# accurate the decision tree is on the test data.  Please use this to test how accurate you are.
def testDecisionStump(trainingData, testData):
    numCorrect = 0
    stump = DecisionStump(trainingData)
    stump.train()

    for i in range(len(testData)):
        label = stump.classify(testData[i][0])
        print("Test value:", testData[i][0], "Our prediction:", label, "Actual label:", testData[i][1])
        if label == testData[i][1]:
            numCorrect +=1
    
    return float(numCorrect) / float(len(testData))


studentDataPure = loadDataFromFile("studentDataPure.p")
stump = DecisionStump(studentDataPure)

error = testDecisionStump(studentDataPure, studentDataPure)
print ("Accuracy of our decision stump on the training data is", str(error*100) + "%")
print ("")

studentTest = loadDataFromFile("studentTest.p")

error = testDecisionStump(studentDataPure, studentTest)
print ("Accuracy of our decision stump on the test data is", str(error*100) + "%")


