# Weighting Mesopotamia

# You are a government leader of Mesopotamia, and Mesopotamia is facing an 
# influx of immigrants, many of whom die, and you want to determine what 
# factors contribute to people dying so that immigrants can make an informed 
# decision. 
#
# The initial settlement is conducting the first 5 year experiment. At the 
# end of the five years, they have their data telling them,the DNA sequence 
# of each individual and whether they survived for five years or not. The 
# data may look something like the following (training set). Note: 
# Mesopotamians had different symbols to represent a DNA strand.
#
# After the first five years, a new group of settlers come in (test set). 
# Their DNA sequence is written down, and the settlers predict whether they
# will live or die based on the DNA sequences and results of the previous 
# experiment. (explained below)
#
# The results are looked at, after five years, and weights are given to 
# each expert depending on whether it predicted correctly.
# This civilization has the following type of data: [“MYDNASTRANDS”, “live”] 


###############################################################################

from math import *
from random import *

############ Training and Test Set ####################
def getDataFromFile(filename):
    with open(filename, 'r') as f:
        data = eval(f.read()) # NOTE: DO NOT USE eval unless you are absolutely
                              # sure that your file is uncorruptable!!!
    return data

############# KNN to get weights of branches ###########

# This distance formula is using the four letters of a string starting at 
# the expert's index to calculate the distance between DNA strings.
# For example ABCD, TYUY we would have ord(A)-ord(T) + ord(B)-ord(Y) ...
def distance(dna1, dna2, expertIndex):
    newDna1 = dna1[expertIndex*4:(expertIndex+1)*4]
    newDna2 = dna2[expertIndex*4:(expertIndex+1)*4]
    total = 0
    for index in range(len(newDna1)):
        total += abs(ord(newDna1[index]) - ord(newDna2[index]))
    return total

# Returns the K closest neighbors to the current test instance
def getNeighbors(trainingSet, testInstance, k, expertIndex):
    # Gather the dna strand of the test instance, and initialize the list
    # of distances.
    distances = []
    testDNA = testInstance[0]
    
    # Here we want to calculate the distance between our current point, and
    # the test point. (Use the helper function)
    # Note, the distance function doesn't require x, y points but the 
    # dna strands and expert index.

    ###################################################################
    # Fill in here
    ###################################################################

    # For our design we will be storing the distances in a 2D List so we 
    # can easily sort them below
        
    distances.sort()
    neighbors = []
    # Here we would like to return only the k closest training instances. 
    # So we will be appending the top 3 distances 

    ###################################################################
    # Fill in here
    ###################################################################

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
    return votes[0]

# Returns True, if the majority of the closest neighbors live, 
# false otherwise
def getLabel(neighbors):
    typeVotes = {}
    # Here we will iterate through neighbors and retrieve the true or false 
    # type of each neighbor and add it to the dictionary type votes.

    ###################################################################
    # Fill in here
    ###################################################################

    typeVotes = sortVotes(typeVotes)
    return typeVotes[1]

def knnMain(trainingSet, testSet, experts):
    k = 3
    penalty = .5
    # Iterate through each instance in the testSet. For each testInstance, we 
    # will also iterate through each expert. From there we will find the 
    # neighbors, labels, and actual label based on that testInstance-expert
    # scenario, and downweight the current expert if the label came back 
    # incorrect.
            
    ###################################################################
    # Fill in here
    ###################################################################

    return experts

# Gather test and training sets
trainingSet = getDataFromFile("data.txt")
testSet = []
for i in range(len(trainingSet)//2):
    testSet.append(trainingSet.pop())

#experts =      ["Speed", "Height", "Weight"]
expertWeights = [1,       1,        1]
knnMain(trainingSet, testSet, expertWeights)
print(expertWeights)


# Challenge 0: For the first step, complete the getNeighbors function which 
# will iterate over the trainingSet call the distance function, and then
# add the distance and traingingInstance to a list similar to last time. 
# Be careful, and make sure to send the correct information in the distance 
# function. Then similarly to our original KNN, retrieve the top k instances 
# from the created 2-D list of distances and points.

# Challenge 1: For the next step, we will be completing the getLabel function.
# We are trying to predict the label ‘live’ or ‘die’, so similarly to the 
# previous KNN, we will iterate through the neighbors, and add the labels to
# our dictionary accordingly.

# Challenge 2: For the final step, you will want to follow a similar format 
# to our previous iteration of KNN. Except in this case (a) you will want to 
# iterate through each expert over each test instance and (b) after you have 
# successfully found the label for the given expert:instance, you want to check 
# if it is correct.
# If it is correct, then leave it, if it is not correct, then you will 
# have to downweight your current expert.

# Make sure you are referencing the previous KNN assignment while you do this!


