#!/usr/bin/env python3
################################################################################
# Stock Shark
#
# Have you heard of the stock market? If so, you probably know that some people
# have gotten VERY rich trading stocks. However, it is not that easy to do.
# It is very difficult to predict the stock market, and therefore hard to know
# when your money will increase or decrease in value. To help with that, we
# will use machine learning to predict whether the S&P 500, an indicator of
# how well the stocks of 500 of the most influential companies, will go up or
# down today, using yesterday's values. Let's see whether machine learning can
# help us become billionaires!
#
# Each element of our training data contains three entries. The first is the
# simple moving average of the daily change in the stock value over the last
# 14 days (float). The second is a string representing whether the stock
# increased ("UP") or decreased ("DOWN") yesterday. The third is a string
# indicating whether the stock increased or decreased today. Your goal is to
# create a decision tree that uses the first two (yesterday's values) to predict
# the last one (today's value). The training data is from every day the stock
# market was open in 2016, and the test data is from every day the stock market
# was open in 2017. Good luck!
#
################################################################################

################################################################################
# DO NOT MODIFY THIS PART OF THE FILE (unless you know what you are doing :P )
#
# However, skim through it to make sure you understand what it is supposed to
# do.
################################################################################
import csv, random

# This class represents a single node in the decision tree. To create a Node,
# do "exampleNode = Node(data)". The data should be the elements of the training data
# that have filtered down to this node. And then to split this node into two
# children, do "exampleNode.setSplit(attributeIndex, value, split1, split2)".
# Attribute index should be the index of the attribute you are splitting on --
# 0 for simple moving average, and 1 for whether the stock went up or down
# yesterday. Value is the value you are splitting on (i.e. if you are
# checking whether the simple moving average is <= 50.0, the index is 0 and
# the value is 50.0). Split1 and split2 are the two splits
class Node(object):
    def __init__(self, trainingData):
        self.trainingData = trainingData
        self.attributeIndex = None
        self.value = None
        self.leftChild = None
        self.rightChild = None

    def setSplit(self, attributeIndex, value, split1, split2):
        self.attributeIndex = attributeIndex
        self.value = value
        self.leftChild = Node(split1)
        self.rightChild = Node(split2)
        return self.leftChild, self.rightChild

# this function takes in a filepath to the stock data, and returns a list of
# 3-tuples representing the data.
def loadDataFromFile(filepath):
    with open(filepath, 'rb') as csvfile:
        fileReader = csv.reader(csvfile)
        data = []
        for row in fileReader:
            if len(row) < 3: break
            data.append((float(row[0].strip()), row[1].strip(), row[2].strip()))
        return data

# this function takes in a decision tree and the test data, and returns how
# accurate the decision tree is on the test data
def testDecisionTree(decisionTree, testData):
    numCorrect = 0
    for data in testData:
        node = decisionTree
        # Keep going down the tree until we reach a leaf
        while not (node.leftChild is None or node.rightChild is None):
            if node.attributeIndex == 1:
                if data[node.attributeIndex] == node.value:
                    node = node.leftChild
                else:
                    node = node.rightChild
            else:
                if data[node.attributeIndex] <= node.value:
                    node = node.leftChild
                else:
                    node = node.rightChild
        # Now, "node" is a leaf. Predict the label at this leaf from the training data
        ########################################################################
        # BONUS CHALLENGE - FILL THIS IN AND UNCOMMENT THE LINES
        #
        # # Similar to getImpurity, calculate the upFraction and downFraction
        # # from node.trainingData
        # randomNumber = random.random() # returns a random float in [0.0, 1.0)
        # if randomNumber < upFraction: # true upFraction of the time
        #     predictedLabel = "UP"
        # else: # true downFraction of the time
        #     predictedLabel = "DOWN"
        ########################################################################
        # BONUS CHALLENGE - Comment out the below line
        predictedLabel = node.trainingData[0][2]

        actualLabel = data[2]
        if predictedLabel == actualLabel: numCorrect += 1
    return float(numCorrect)/float(len(testData))

# Splits the dataset into two, and returns the two lists. If the attributeIndex
# is 1, split1 will contain those data points where yesterday's change is ==
# to value, and split2 will contain the points that were not equal to value.
# If attributeIndex is 0, split1 will contain the points whose simple moving
# average is <= value, and split2 will contain the points whose simple moving
# average is > value.
def splitData(dataset, attributeIndex, value):
    split1, split2 = [], []
    for data in dataset:
        # Index 1 has only two values, "UP" or "DOWN". Therefore, we want to
        # compare it with ==, not <=.
        if attributeIndex == 1:
            if data[attributeIndex] == value:
                split1.append(data)
            else:
                split2.append(data)
        # Index 0 has infinite float values, so we want to compare it with <=
        # and not ==
        else:
            if data[attributeIndex] <= value:
                split1.append(data)
            else:
                split2.append(data)
    # Return the splits
    return split1, split2

################################################################################
# WRITE YOUR CODE BELOW THIS
################################################################################

# Returns a float that represents the impurity of the data, according to the
# Gini Impurity
def getImpurity(dataset):
    ############################################################################
    # FILL THIS IN
    ############################################################################

# evaluateSplit takes in three lists -- the overall data list, and the two lists
# it is split into. It then returns a float corresponding to how good the
# split is
def evaluateSplit(dataset, split1, split2):
    ############################################################################
    # FILL THIS IN
    ############################################################################


# generates the best split of the data. It returns the attributeIndex to split on,
# the value of the split, and the two resulting lists after splitting along
# that attributeIndex and value.
def generateBestSplit(dataset):
    # Initialize variables to keep track of the best split we have seen so far
    minImpurity = None
    minAttributeIndex = None
    minValue = None
    minSplit1 = None
    minSplit2 = None
    # First, try splitting along the first attribute (index 0)
    sortedDataset = sorted(dataset) # sort it so that every value except the max can be used as a splitting point
    splitOptionsFirstAttribute = [sortedDataset[i][0] for i in range(len(dataset)-1)]
    for value in splitOptionsFirstAttribute:
        split1, split2 = splitData(dataset, 0, value) # Remember, the second attribute is at index 1!!!
        impurity = evaluateSplit(dataset, split1, split2)
        if (minImpurity is None or impurity < minImpurity): # we found a better split!
            minImpurity = impurity
            minAttributeIndex = 0
            minValue = value
            minSplit1 = split1
            minSplit2 = split2
    # Next, write code to split along the second attribute (index 1)
    ############################################################################
    # FILL THIS IN
    ############################################################################
    return minAttributeIndex, minValue, minSplit1, minSplit2

# This function takes in a node, and checks if its trainingData is fully pure
# (base case). If not, it generates the best split of that training data,
# sets that split for the node to get its new left and right children, and
# calls itself recursively on the two children.
def createDecisionTreeRecursive(node):
    ############################################################################
    # FILL THIS IN
    ############################################################################

# Initializes the decision tree with the starting node, then calls the recursive
# function to build the rest of the decision tree
def createDecisionTree(trainingData):
    startingNode = Node(trainingData)
    createDecisionTreeRecursive(startingNode)
    return startingNode

# First, get the training data
trainingData = loadDataFromFile("trainingData.csv")
# Then, create the decision tree
decisionTree = createDecisionTree(trainingData)

# Now, get the test data
testData = loadDataFromFile("testData.csv")
# Test the decision tree on the test data
accuracy = testDecisionTree(decisionTree, testData)
print("Accuracy: "+str(accuracy))


# CHALLENGE 0 - The first part of any problem that uses data is to understand
# the dataset. Go to where we load the training data in this file (near the
# end of the code), and print the trainingData. Make sure you understand
# what the data is, and how to interact with it (ask a friend or mentor for
# help if you are unsure).


# CHALLENGE 1 - Next, write the getImpurity function. In this function, you
# should first determine the number of points in the dataset with the
# "UP" label, and the number of points with the "DOWN" label (be sure one to
# get confused between yesterday's UP/DOWN labels, which are ar index 1, and
# today's UP/DOWN labels, which are at index 2). Once you have the number of
# points, calculate the fraction of points in the dataset that have the up label
# and the down label. Finally, use that to calculate the impurity, using the Gini
# Impurity measure we taught in class.


# CHALLENGE 2 - If you recall, the decision tree algorithm consists of finding
# the best splitting point, splitting the data, and continuing from there until
# you have perfectly separated the data. We have written the splitData function
# for you, which takes in the dataset, an attribute index to split on, and a
# value at which to split, and splits the dataset into two. Read through the
# splitData function, and make sure you understand what it is doing. Ask a mentor
# if you are unsure.


# CHALLENGE 3 - The next step is to write the evaluateSplit function. Remember,
# this is a weighted average of the impurities in both splits, weighted by
# the fraction of the elements from the original data that is in each split.
# In other words, return the split1 impurity times the split1 fraction, plus the
# split2 impurity times the split2 fraction.


# CHALLENGE 4 - Now the next step is to generate the best split. We do so by
# trying every single splitting point, for every single attribute, and keeping
# track of which results in the least impure splits. We have given the code for
# evaluating the least impure of all aplits aloung the first attribute, the
# simple moving average. Now, write the code to evaluate a better split (if one
# exists) along the second attribute. HINT: most of the code should be the
# same as the first attribute -- you just have to change the attribute index and
# the attribute options.


# CHALLENGE 5 - Finally, we are going to write the core logic of a decision tree
# that differetiates it from a decision stump -- namely, the recursion. Fill in
# createDecisionTreeRecursive. This function should take in a node. First, it
# should check if that node's training data is fully pure (base case), and if
# so, return. If not, it shoudl generate the best split along the training data,
# set that split on the node to get its two split left and right children, and
# then call itself recursively on the left and right children. Note that this
# function down not have to return anything, since it mutably modifies the node
# (ask a mentor if you are curious about what this means).
#
# NOTE: Make sure to keep the order of split1 and split2 the same -- don't mix
# them up! Also, be sure to NOT call setSplit on a leaf node (i.e. a node with
# perfect purity)!


# BONUS CHALLENGE - Every dataset will have some data that represents trends,
# and other data that represents noise (random deviations in the dataset). A
# good machine learning algorithm should learn the trends from the data, but
# not the noise (because if the algorithm customizes itself to something that
# was just due to random chance, then it won't perform as well on future data).
# The act of learning something in the data that was actually due to randomness
# and not a trend is called overfitting.
#
# Overfitting is a big problem with decision trees, since we keep growing the
# tree until every single leaf contains a pure subset of the training data.
# Therefore, we are bound to hardcode some of the noise into our decision tree.
# One way to get around that is by limiting the depth of the decision tree.
# Add two additional parameters to the recursive function, maxDepth and
# currentDepth. Then, modify the recursive function so the tree stops growing
# not only when the impurity is 0, but also when we have exceeded maxDepth.
# In other words, you are modifying the base case of the recursive function.
#
# After modifying the recursive function, you also have to modify how we use the
# decision tree to make predictions. Now, just being at a leaf does not guarentee
# that we have one set label (since some leaves may contain UP and DOWN values).
# Therefore, we have to modify the way we predict a label by looking at what
# fraction of the data at that node is UP, what fraction is DOWN, and picking
# a random label which is UP or DOWN that appropriate fraction of the time.
# Make this modification in the testDecisionTree function.
#
# Lastly, modify the createDecisionTree function, where the recursive function
# is called.
#
# Finally, test it out. Play around with different max depths and look at the
# corresponding accuracy. What was the overall depth of the tree before this
# change? Which depth has the best accuracy? What does that tell you about
# overfitting?


# COMPREHENSION QUESTIONS - think about these and/or discuss them
# with a friend. We will discuss them at the end of class.
#    - As you saw, the accuracy of our decision tree is around 50%. That is as
#      bad as if we tossed a coin and predicted "UP"/"DOWN"! What does this
#      tell you about making stock market predictions using historical data?
#      Do you have any ideas for other data we could take into account to make
#      a better predictor?
#    - All of our training data came from 2016 and all of our test data came
#      from 2017. What are the pros/cons of doing this?
#    - When splitting along the first attribute (simple moving average), we try
#      every possible split. However, the number of splits is very large
#      (equivalent to the size of the training data minus one). Do you have any
#      ideas for a faster way to evaluate splits, that may not get us the best
#      split but will get us a good enough split (there are many options).
#    - What if instead of each split being binary (i.e. yes or no), some had
#      more options. For example, if instead of UP/DOWN for the second attrbute,
#      we had UP/DOWN/SAME, then we may have to have 3-way splits. What parts of
#      the code would we have to modify to account for this?
#    - Decision trees in general  are useful in day-to-day life. Fundamentally,
#      they are just a way of organizing cascading conditions (i.e. if I do X,
#      then I will go down this rout of the tree). Think of ways in which
#      decision trees might be useful in your life, or the lives of people you know.
