import numpy as np
import math

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




#This is the 2d list of all of the student's temperatures along with the diagnosis of cold or fever
#that they had.  The first value in each of the lists within the list is the temperature.  The second value
#is the label of "cold" or "flu".  A 0 denotes cold and a 1 denotes flu. 


studentDataPure = [
[101.2, 1], 
[98.0, 0], 
[99.1, 1], 
[99.8, 1], 
[100.0, 1], 
[98.3, 0], 
[101.7, 1], 
[100.7, 1], 
[98.9, 0], 
[98.6, 0], 
[99.4, 0], 
[100.3, 1],
[102.1, 1],
[101.8, 1]] 

studentDataUnpure = [
[101.2, 1], 
[98.0, 0], 
[99.1, 1], 
[99.8, 1], 
[100.0, 0], 
[98.3, 0], 
[101.7, 1], 
[100.7, 1], 
[98.9, 0], 
[98.6, 1], 
[99.4, 0], 
[100.3, 1],
[102.1, 1],
[101.8, 1]]

studentTest = [
[99.5, 1],
[97.8, 0],
[100.1, 1],
[99.0, 1],
[100.8, 1,
[98.0, 0],
[99.2, 1],
[101.0, 1,
[97.6, 0],
[100.4, 1],
[98.1, 0],
[101.3, 1],
[97.5, 0],
[99.8, 1],
[100.2, 1],
]
 






#This function takes in a 2d list and sorts them from the first value in each list within.

def sortByAscendingTemp(data):
	sortedData = sorted(data)
	return sortedData





#Challenge #1: Please write a function that takes in the 2d list studentDataPure and finds the optimal temperature
#that divides the diagnosis of flu or cold in the file.
#Challenge #2: Please write a function that takes in the 2d list studentDataUnPure and finds the optimal
# temperature that divides the diagnosis of flu or cold in the file.

def findOptimalDivide(data):

	return 0


#Challenge #2 With the dividing point, classify the following students as either flu or cold.  Tie of the dividing temperature goes to cold.  Your predictions should end up being 100% correct.

def decisionStump(dividingTemp, studentTest):

    return 0

























			









