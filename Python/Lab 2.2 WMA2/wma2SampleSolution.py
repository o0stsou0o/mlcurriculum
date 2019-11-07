#!/usr/bin/env python3
import matplotlib.pyplot as plt

################################################################################
# Weather Predictor
#
# There has been a war and the whole world is decimated. You and 10 other
# friends are the only people alive, and you are all split up across major
# cities around the world. In order to survive, you need to understand the
# environment that you are in. And in order to understand that, you need to
# know the weather. All weather prediction equipment from your city is gone,
# and all you have is a radio to communicate with your friends. Everyday, they
# tell you the weather in their city, and you have to use that to predict the
# weather in your city. You decide to use the weighted majority algorithm to
# do it.
#
################################################################################

# Takes in a city name and imports the corresponding data file
def getCityData(cityName):
    prefix = "/Users/amal/Documents/Teknowledge/Curriculum/machine_learning_curriculum/weatherDatasetByDays/"
    suffix = ".txt"
    filename = prefix + cityName + suffix
    with open(filename, 'r') as f:
        data = eval(f.read()) # NOTE: DO NOT USE eval unless you are absolutely
                              # sure that your file is uncorruptable!!!
    return data

# Set your city name and the expert city names
myCity = "Pittsburgh"
expertCities = ["Beijing", "Cairo", "Delhi", "Mexico_City", "Mumbai", "New_York", "Osaka", "Sao_Paulo", "Shanghai", "Tokyo"]

# Convert city names to city data
myCityData = getCityData(myCity)
expertCityData = {city : getCityData(city) for city in expertCities}
# print(myCityData, expertCityData)
# Note that expertCityData is a dictionary, where the key is a city name and
# the value is a list (of size 365) of the average weather on that day

# Initialize expert weights here, as a dictionary that maps from city name to
# the initial expert weight.
expertWeights = {city : 1.0 for city in expertCities} # FILL THIS IN

# Weather Labels
# 0 - Sunny
# 1 - Cloudy
# 2 - Rain
# 3 - Snow
numberOfWeatherLabels = 4

# The amount to reduce expert weights by each time they are wrong
penalty = 0.5 # This can be any value between 0.0 and 1.0

# Variables for graphing loss (BONUS CHALLENGE)
predictionLoss = []
expertLosses = {city : [] for city in expertCities}

for day in range(len(myCityData)):
    # Initialize the variables that will store expert predictions and the
    # overall weight assigned to each weather
    expertPredictions = {city : None for city in expertCities} # FILL THIS IN
    weatherCount = {i : 0.0 for i in range(numberOfWeatherLabels)} # FILL THIS IN
    # Iterate over every expert, and get their prediction (the weather in that
    # city on the specific day)
    for expertCityName in expertCities:
        ########################################################################
        prediction = expertCityData[expertCityName][day]
        expertPredictions[expertCityName] = prediction
        weatherCount[prediction] += expertWeights[expertCityName]
        ########################################################################

    # Find the weather label that had the max count in "weatherCount"
    ############################################################################
    maxWeather, maxCount = None, -1.0
    for weather, count in weatherCount.items():
        if count > maxCount:
            maxWeather = weather
            maxCount = count
    ############################################################################
    predictedWeather = maxWeather # Set this to the weather label that had the max count

    # Get the actual weather
    actualWeather = myCityData[day]

    # Add to prediction loss (BONUS CHALLENGE)
    if predictedWeather != actualWeather:
        predictionLoss.append(1.0)
    else:
        predictionLoss.append(0.0)

    # Re-weight the experts
    ############################################################################
    for expertCityName, expertPrediction in expertPredictions.items():
        if expertPrediction != actualWeather:
            expertWeights[expertCityName] *= penalty
            # Add the expert loss (BONUS CHALLENGE)
            expertLosses[expertCityName].append(1.0)
        # Add the expert loss (BONUS CHALLENGE)
        else:
            expertLosses[expertCityName].append(0.0)
    ############################################################################

################################################################################
for expertCityName, expertWeight in expertWeights.items():
    print(expertCityName, expertWeight)
################################################################################

################################################################################
# BONUS CHALLENGE UNCOMMENT THIS

# Convert Loss to Cumulative Loss
predictionCumulativeLoss = [0.0]
for loss in predictionLoss:
    predictionCumulativeLoss.append(predictionCumulativeLoss[-1] + loss)
expertCumulativeLosses = {city : [0.0] for city in expertCities}
for expertCityName, expertLoss in expertLosses.items():
    for loss in expertLoss:
        expertCumulativeLosses[expertCityName].append(expertCumulativeLosses[expertCityName][-1] + loss)

# Convert Cumulative Loss to Average Cumulative Loss
predictionAverageCumulativeLoss = [predictionCumulativeLoss[t+1]/(t+1) for t in range(len(predictionCumulativeLoss)-1)]
expertAverageCumulativeLosses = {city : [expertCumulativeLosses[city][t+1]/(t+1) for t in range(len(expertCumulativeLosses[city])-1)] for city in expertCities}

# Plot the Cumulative Losses
fig, ax = plt.subplots()
ax.set_title("Average Cumulative Loss for " + myCity + " Weather")
expertColors = ["red", "orange", "yellow", "green", "turquoise", "purple", "pink", "indigo", "brown", "black"]
i = 0
for expertCityName, expertAverageCumulativeLoss in expertAverageCumulativeLosses.items():
    color = expertColors[i]
    ax.plot(range(1, len(expertAverageCumulativeLoss)+1), expertAverageCumulativeLoss, color=color, label=expertCityName)
    i += 1
color = "blue"
ax.plot(range(1, len(predictionAverageCumulativeLoss)+1), predictionAverageCumulativeLoss, color=color, label="WMA")
ax.set_xlabel("Timesteps")
ax.set_ylabel("Average Loss")
ax.grid()
ax.legend(loc='center left', bbox_to_anchor=(0.90, 0.5))
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()
################################################################################


# CHALLENGE 0 - Change the "prefix" variable in the "getCityData" function to
# the path to the folder where the city data is located. Remove your city from
# the expertCities list and set it to the "myCity" variable. Then, print out
# myCityData and expertCityData to understand the dataset. The data for each
# city is a list of size 365, with integers from 0-3. The integers represent
# the weather on that day of 2017, where 0 is sunny, 1 is cloudy, 2 is rainy,
# and 3 is snowy.


# CHALLENGE 1 - Initialize the expert weights variable. Although in the previous
# activity we had one separate variable for each expert weight, we cannot do
# that with 10 experts (too many variables!) Therefore, we will store all expert
# weights in a dictionary, that maps from city name to initial weights (1.0).


# CHALLENGE 2 - In the previous activity, we had one separate variable to store
# each expert prediction, and to store the sum of the weights of the experts
# that made each prediction (i.e. the sum of weights of experts that predicted
# True and False). This time, since we have 10 experts and 4 labels, we will
# store these in dictionaries.
#      1) Initialize the "expertPredictions" variable as a dictionary that maps
#         from city name to None (since they have not yet made a prediction).
#      2) Initialize the "weatherCount" variable as a dictionary that maps from
#         each weather label (an int from 0 to 3), to 0.0 (since no expert has
#         currently predicted that weather).
#      3) Now, implement the logic inside the for loop, where you get the
#         prediction for that expert (i.e. that expert's weather on the specific
#         day), add it to the "expertPredictions" dictionary, and add that
#         expert's weight to the count for its prediction in "weatherCount."


# CHALLENGE 3 - We now have to find the weather that had the largest sum of
# expert weights (that weather will be our prediction). Iterate over the
# "weatherCount" dictionary (using "weatherCount.items()"), storing the
# maxCount you have seen so far as well as the corresponding weather label.
# That weather will be the weather the algorithm will predict.


# CHALLENGE 4 - Now that we know what all the experts predicted and what the
# actual weather was in our city, re-weight all the experts. Iterate over the
# expertWeights dictionary, and multiple each weight by penalty if the expert
# prediction was not equal to the actual weather.


# CHALLENGE 5 - The algorithm is all coded up! Finally (outside the for loop),
# iterate over the "expertWeights" dictionary and print out the city name and
# weights. Then run your code, debug, and see if the weights you get are
# logical (higher weights mean a greater similarity between city weather).
# If your weights make sense, check them against our answers.


# BONUS CHALLENGE - If we were to actually use this system as a weather
# predictor, how well would it perform? To understand this, we use a notion
# called loss, which is a measure of how bad a prediction is. In this case,
# for every day let us say the loss is 1.0 if the prediction is wrong and 0.0
# if the prediction is correct (called a zero-one loss). What we want to do is
# understand the cumulative loss over time of our weighted majority prediction,
# as well as the other experts (ideally, weighted majority will be the best).
#
# To do this, we need to store the loss that our predictor and each expert
# recieve every day. Create a list, "predictionLoss", and a dictionary of lists,
# "expertLosses". At every time step, append onto "predictionLoss" 1.0 if the
# predicted weather and actual weather are the same, and 0.0 otherwise. At every
# timestep, for every expert, append onto its corresponding value in
# "expertLosses" a 1.0 or 0.0 depending on whether that expert's prediction
# was wrong or not. In the end, "predictionLoss" should be a list of size 365,
# and "expertLosses" should be a dictionary where the keys are city names and
# each value is a list of size 365. HINT: You should not have to add more than
# 5 lines of code for this.
#
# Now, uncomment the lines of code at the bottom of the code, and run. If all
# worked well, you should get a graph of how the average cumulative loss of your
# algorithm compared to each expert. Try to find interesting trends in the graph.


# COMPREHENSION QUESTIONS - think about them and/or discuss them
# with a friend. We will discuss them at the end of class.
#    - Intuitively, the weights represent a measure of similarity -- how similar
#      that city's weather is to your city's weather. The way we measure this
#      is by starting at 1.0 and multiplying it by penalty for every day that
#      city's weather differs from your city's weather. What are strengths and
#      shortcomings of this similarity measure? What are other ways you can
#      measure the similarities between two city's weather?
#    - If City A's weight for City B is X, can you say anything about City B's
#      weight for City A? Why or why not?
#    - If you got to the BONUS CHALLENGE, you saw that we used a zero-one loss
#      to measure the effectiveness of our prediction system. What are strengths
#      and shortcomings of this loss? How else can we measure loss?
