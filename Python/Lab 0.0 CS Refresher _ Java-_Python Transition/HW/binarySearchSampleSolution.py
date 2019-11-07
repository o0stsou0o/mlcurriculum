################################################################################
# Homework 0 - Binary Search
#
# In this homework, you will be writing a common search algorithm, binary
# search. Step-by-step instructions for each challenge are at the BOTTOM of
# this file. Please complete the challenges, and email us at
# cmu.teknowledge@gmail.com if you have any questions (please email us -- we
# love getting questions)!
#
################################################################################

# Takes in a list l (can be sorted or unsorted) and an elem, and searches the
# list for elem using linear search. If elem is in the list, it returns the
# index of elem. If not, it returns -1.
def findLinearSearch(l, elem):
    # Iterate over all the indices in the list
    for i in range(len(l)):
    # Return the index of the element if the element
    # is found
        if (l[i] == elem):
            return i
    # return -1 if the element is not found
    return -1

# Takes in a list l (MUST be sorted) and an elem, and searches the  using
# binary search. list for elem. If elem is in the list, it returns the index
# of elem. If not, it returns -1.
def findBinarySearch(l, elem):
    ############################################################################
    # CHALLENGE 1 - FILL THIS IN
    lo = 0
    hi = len(l)-1
    ############################################################################
    while (lo <= hi):
        ########################################################################
        # CHALLENGE 2 - FILL THIS IN
        mid = (lo + hi)//2
        ########################################################################

        ########################################################################
        # CHALLENGE 3 - FILL THIS IN
        if (l[mid] == elem):
            return mid
        ########################################################################

        ########################################################################
        # CHALLENGE 4 - FILL THIS IN
        if (l[mid] < elem):
            lo = mid + 1
        else:
            hi = mid - 1
        ########################################################################

    # if we reach here, then element was not present
    return -1;

################################################################################
# CHALLENGE 0 - Below is a sample of binary search being run on a list, and which
# elements you check in which order. After that, there is another sample list.
# Below it, write the order in which you will check elements. If the list does
# not have a whole number mid point, round it down (for example, in [2, 4, 7, 9],
# I would check 4).
#
# List: [1, 2, 3, 4, 5, 6, 9, 13, 27] Element: 4
# Step 1: Remaining List: [1, 2, 3, 4, 5, 6, 9, 13, 27]. Check 5. 4 < 5, so LEFT side
# Step 2: Remaining List: [1, 2, 3, 4]. Check 2. 4 > 2, so RIGHT side
# Step 3: Remaining List: [3, 4]. Check 3. 4 > 3, so RIGHT side
# Step 4: Reaminaing List: [4]. Check 4. 4 == 4, so DONE
#
# List: [-3, 0, 5, 8, 9] Element: 9
# Step 1: Remaining List: [-3, 0, 5, 8, 9]. Check 5. 9 > 5, so RIGHT side
# Step 2: Remaining List: [8, 9]. Check 8. 9 > 8, so RIGHT side
# Step 3: Remaining List: [9]. Check 9. 9 == 9, so DONE
################################################################################


################################################################################
# CHALLENGE 1 - We will now write the code for binary search. First, we need to
# keep track of our remaining list. We do this by creating two new variables,
# "lo" and "hi". lo will be the bottom index of our remaining list, and hi will
# be the top index of our remaining list. Initially, we want our whole list to
# be remaining, so initilize lo to be 0 and hi to be the length of the list
# minus one.
################################################################################


# Note that we want to keep looping until the remaining list is of
# size 0. This is not a fixed number of iterations -- for longer lists, we will
# iterate longer. Therefore, we used a while loop instead of a for loop.


################################################################################
# CHALLENGE 2 - We now need to calculate the middle element of the remaining list.
# We will do so by taking the average (arithmetic mean) of lo and hi, and rounding
# down. As you know, in CS there is an easy way to round down while dividing,
# called integer division. This automatically divides and rounds down. For
# example, in python 3//2 is 1, 4//2 is 2, and 5//2 is 2. You should use this
# when calculating the average and rounding down.
################################################################################


################################################################################
# CHALLENGE 3 - Now that we have the middle index, we need to check if the
# element at that index is greater than (<), less than (<), or equal to (==)
# the element we want. We will first check ==. Complete the if statement
# and the line below it. Remember to use square brackets when accessing the
# element at a index in a list (i.e. l[0] is the first element of a list).
################################################################################


################################################################################
# CHALLENGE 4 - If we reach this point in the code, we know the middle element
# is not equal to the element we want (if it were, we would have returned).
# This time, we will use an if-else statement.
#
# First, fill in the if statement to check whether the element at the mid
# index is < the element we want to find. If so, you want to ignore the top
# half of the list. So set hi to mid minus one (minus one because you have
# already checked mid so don't want to include it in the remaining list).
#
# In the line after the else statement, we know that the element we want is
# greater than the mid element. So we want to ignore the bottom half, so
# should set lo to min plus one. Remember to index the lines after an if
# statement and else statement.
################################################################################


################################################################################
# CHALLENGE 5 - You are now done! Run it, and see how you did (we have code
# that automatically runs test cases below).
#
# If you have errors, read what they are. Python not only gives you a brief
# description of the error (bottom line of the error message) but also tells
# you what line it is on (third to bottom line of the error message).
#
# To debug your code, the best thing is to use print statements. For example,
# if at the beginning of every loop (after setting mid), you have the line
# print(lo, mid, hi) , you will be able to see how those variables change.
# You can then run through the example in the test function by hand, to see if
# that is correct. You can also add prints inside the body of an if statement,
# to see if that statement was true (remember to indent all lines of code in
# the body of the if statement).
################################################################################


# Tests our binary search function. Remember that the input lists must be sorted.
def testBinarySearch():
    print("Testing Binary Search...")
    numCorrect = 0
    numTotal = 0
    l = [2, 3, 4, 10, 40]
    if (findBinarySearch(l, 2) == 0):
        numCorrect += 1
    numTotal += 1
    if (findBinarySearch(l, 5) == -1):
        numCorrect += 1
    numTotal += 1
    if (findBinarySearch(l, 40) == 4):
        numCorrect += 1
    numTotal += 1
    if (findBinarySearch(l, 4) == 2):
        numCorrect += 1
    numTotal += 1
    l.append(80)
    if (findBinarySearch(l, 4) == 2):
        numCorrect += 1
    numTotal += 1
    if (findBinarySearch(l, 10) == 3):
        numCorrect += 1
    numTotal += 1
    if (findBinarySearch(l, 80) == 5):
        numCorrect += 1
    numTotal += 1
    if (findBinarySearch(l, 81) == -1):
        numCorrect += 1
    numTotal += 1
    print("Finished Testing Binary Search...")
    print("Num Correct: %d / %d" % (numCorrect, numTotal))

testBinarySearch()
