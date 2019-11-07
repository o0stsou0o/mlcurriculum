################################################################################
# Supernova 
#
# We have data on about 500 stars in the universe. We have the age at which
# they died in millions of years, and the temperature at which they died in 
# millions of degrees. The other most important data point is whether or not
# that star supernova'd or not upon death.
#
# One at a time you are going to go through your test set to see whether you can
# correctly predict whether a star will supernova or not based on stars closest 
# to it with the training set given. This is following the KNN algorithm. From
# the main function we will return how accurate our test set is at predicting
# whether a star will supernova or not given said information about the star.
#
################################################################################

from math import *
from random import *

# This code retrives the data from the data.txt file
############ Training and Test Set ####################
def getDataFromFile(filename):
    with open(filename, 'r') as f:
        data = eval(f.read()) # NOTE: DO NOT USE eval unless you are absolutely
                              # sure that your file is uncorruptable!!!
    return data

# Here we randomly pull half of the data out to use as our test set.
trainingSet = getDataFromFile("data.txt")
testSet = []
for i in range(len(trainingSet)//2):
    testSet.append(trainingSet.pop())


############# KNN  ###########

# Helper function to return the euclidean distance of the points on a 2-D grid.
def distance(x0, y0, x1, y1):
    dx = x1-x0
    dy = y1-y0
    return sqrt((dx**2)+(dy**2))

# Returns the K closest neighbors to the current test instance
def getNeighbors(trainingSet, testInstance, k):
    # Gather the x, y points of the test instance, and initialize the lists
    # of distances.
    distances = []
    x0 = testInstance[0]
    y0 = testInstance[1]

    #Iterate through the entire training set
    for trainingInstance in trainingSet:
        # Here we want to calculate the distance between our current point, and
        # the test point. (Use the helper function)
        x1 = trainingInstance[0]
        y1 = trainingInstance[1]
        dist = distance(x0, y0, x1, y1)
        # For our design we will be storing the distances in a 2D List so we 
        # can easily sort them below
        distances.append([dist, trainingInstance])
    distances.sort()
    neighbors = []
    # Here we would like to return only the k closest training instances. 
    # So we will be appending the top 3 distances 
    for index in range(k):
        neighbors.append(distances[index][1])
    return neighbors

# Helper function for sorting the votes in a dictionary
def reverseSort(votes):
    return sorted(votes)[::-1]

# Sort the votes from the dictionary into a 2d list
def sortVotes(typeVotes):
    votes = []
    for key in typeVotes:
        votes.append([typeVotes[key], key])
    votes = reverseSort(votes)
    return votes[0][1]

# Returns True, if the majority of the closest neighbors supernova, 
# false otherwise
def getLabel(neighbors):
    typeVotes = {}
    for neighbor in neighbors:
        # Here we want to retrieve the true or false type of each neighbor
        # and add it to the dictionary type votes.
        curNeighbor = neighbor[2]
        typeVotes[curNeighbor] = typeVotes.get(curNeighbor, 0) + 1
    newLabel = sortVotes(typeVotes)
    return newLabel

# Returns the accuracy of our testSet at determining whether a star will
# supernova.
def knnMain(trainingSet, testSet, k):
    total = len(testSet)
    correct = 0
    for testInstance in testSet: 
        # Iterate through the test set, 1st getting the neighbors, then getting
        # the label, then checking if the actual label is the label returned.
        # If it is, then you can increment correct by 1.
        neighbors = getNeighbors(trainingSet, testInstance, k)
        label = getLabel(neighbors)
        actualLabel = testInstance[2]
        if (label == actualLabel):
            correct += 1
    accuracy = (correct/total)*100
    return accuracy


# Returns Accuracy
k = 3
print(knnMain(trainingSet, testSet, k))


# Challenge 0: Run the code and print out the testSet and trainingSet a few 
# times. Notice how the data is set up: 
# [[ageOfStarAtDeath, tempOfStarAtDeath, superNova?]....]

# Remember: The goal of this function is to test how accurate our algorithm is
# at prediciting a supernova or not.

# Challenge 1: The first step is to complete the function getNeighbors. 
# We are going to calculate the distance between the current test instance
# and every point in the training instance, put them in a list, then sort them.
# Then we will pick the top k elements from the list.

# Challenge 2: The next step is to complete the getLabel function. In this 
# function we are iterating through the returned neighbors, and getting the 
# true or false label and adding that label to our dictionaries.

# Challenge 3: The last step is to iterate through the test set in the knnMain
# function. First gather your neighbors using the getNeighbors helper function.
# Then, get the label, using the getLabel helper function. Then check whether 
# the label retrieved matches the actual label and increment correct 
# accordingly.

