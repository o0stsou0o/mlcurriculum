def getDataFromFile(filename):
    with open(filename, 'r') as f:
        data = eval(f.read()) # NOTE: DO NOT USE eval unless you are absolutely
                              # sure that your file is uncorruptable!!!
    return data

trainingSet = getDataFromFile("data.txt")
testSet = []

for i in range(len(trainingSet)//2):
    testSet.append(trainingSet.pop())

probs = {'Speed': {'Fast': [0,0], 'Medium': [0,0], 'Slow': [0,0]},
                 'Height': {'Tall': [0,0], 'Average': [0,0], 'Smaller than a breadbox': [0,0]},
                 'Weight': {'10lbs': [0,0], '100lbs': [0,0], '1000lbs': [0,0]}
                }

# Getting correct probabilities
for element in trainingSet:
    outcome = element[1] # Live or die
    descriptors = element[2]
    for chars in descriptors:
        curChar = descriptors[chars]
        probs[chars][curChar][1] += 1 # Total current characteristic
        if (outcome == "live"):
            probs[chars][curChar][0] += 1

for chars in probs:
    for curChar in probs[chars]:
        liveAndCurChar = probs[chars][curChar][0] 
        totalCurChar = probs[chars][curChar][1]
        if (totalCurChar == 0):
            probs[chars][curChar] = 0
        else:
            probs[chars][curChar] = liveAndCurChar/totalCurChar

print(probs)


