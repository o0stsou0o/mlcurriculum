#!/usr/bin/env python3

################################################################################
# Movie Predictor
#
# You have two friends who want to recommend new movies to you. However, you
# are not sure which friend's movie preferences better align with yours. To
# determine this, you create a test.
#
# You come up with a list of old movies that you have seen. One at a time, you
# ask your two friends whether they liked them. You also know whether you liked
# the movies. Therefore, using the weighted majority algorithm, you keep track
# of weights, which indicate how well-aligned each friends' preferences are to
# yours. In the end, you can use these weights to determine how much to trust
# each friend when they recommend future movies to you!
#
################################################################################

# This function takes in a string which represents a yes/no question, asks for
# user input, and returns a boolean value indicating whether the use answers
# yes or no.
def getUserInput(prompt):
    print(prompt)
    print("Answer Y/n: ")
    answer = input("> ")
    if (answer[0].lower() == "y"):
        return True
    else:
        return False

# Two experts
expert0Weight = 1.0
expert1Weight = 1.0

# How much the expert weight gets reduced by per wrong prediction
penalty = 0.5 # this has to be >= 0.5. Why?

oldMovies = ["Zootopia",
             "Big Hero 6",
             "Catching Fire",
             "Star Wars: The Phantom Menace",
             "Harry Potter and the Deathly Hallows"]

for movie in oldMovies:
    # First, get expert predictions using the getUserInput function
    expert0Label = getUserInput("Expert 0: Did you like " + movie + "?")
    expert1Label = getUserInput("Expert 1: Did you like " + movie + "?")

    # Next, use the expert weights and expert labels to determine
    # which label you will predict, True or False.

    ############################################################################
    trueWeight = 0.0
    falseWeight = 0.0
    # Get Expert Input
    if (expert0Label == True):
        trueWeight += expert0Weight
    else:
        falseWeight += expert0Weight
    if (expert1Label == True):
        trueWeight += expert1Weight
    else:
        falseWeight += expert1Weight
    ############################################################################

    if (falseWeight > trueWeight): # Fill this in
        predictedLabel = True
    else:
        predictedLabel = False

    # Get Main Character Input
    actualLabel = getUserInput("Main Character: Did you like " + movie + "?")

    # Lastly, for each expert that is wrong, reduce their weight by the
    # penalty amount defined above.

    ############################################################################
    if (expert0Label != actualLabel):
        expert0Weight *= penalty
    if (expert1Label != actualLabel):
        expert1Weight *= penalty
    ############################################################################

    # Uncomment this for debugging
    # print("Expert 0 Weight: " + str(expert0Weight))
    # print("Expert 1 Weight: " + str(expert1Weight))


# Challenge 0: Change the oldMovies list to contain recent movies that you and
# your friends know.


# Challenge 1: The first step is to use the expert labels and weights to
# determine which label to predict. In other words, you will take the weighted
# sum of experts who say True and the weighted sum of experts who say False,
# and predict the label corresponding to whichever is greater. Intuitively,
# this prediction represents "if you were to listen to your friends, would you
# watch this movie or not?"


# Challenge 2: After getting the actualLabel (which represents whether or not
# you liked the movie), the next step is to adjust the expert weights based
# on whether or not their label was accurate. In other words, for any expert
# who made a suggestion that did not align with yours, lower their weight by
# a factor of "penalty." For experts who suggested the same label as you,
# keep their weight the same.


# Challenge 3: Now that all the code is in place, run it and debug it until it
# works. It may help to uncomment the two lines that print the expert weights.


# Challenge 4: COMPREHENSION QUESTIONS -- think about them and/or discuss them
# with a friend. We will discuss them at the end of class.
#    - Do we ever use predictedLabel? What are example scenarios where
#      predictedLabel is important?
#    - Explain in English what the expert weights represent in this scenario.
#      In particular, what does a larger expert weight mean and what does a
#      smaller expert weight mean?
#    - With just two experts, it may not be fair to expect any one expert's
#      movie preferences to completely align with yours. Maybe someone's
#      preferences align with yours when it comes to action movies, but not
#      romance movies. How can you modify WMA to account for preferences by
#      movie genre? (If you have extra time, code it up!)
#    - It is easy to think of real life scenarios where humans can use WMA.
#      What are some real-life scenarios where robots could use WMA? What
#      about where computers and/or machine learning algorithms that are
#      processing tons of data could use WMA?
