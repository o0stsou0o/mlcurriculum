def getDataFromFile(filename):
    with open(filename, 'r') as f:
        data = eval(f.read()) # NOTE: DO NOT USE eval unless you are absolutely
                              # sure that your file is uncorruptable!!!
    return data

############ Training and Test Set ####################
trainingSet = getDataFromFile("data.txt")
testSet = []
for i in range(len(trainingSet)//2):
    testSet.append(trainingSet.pop())

############ Probabilities ############################
probs = getDataFromFile("probs.txt")




from math import *
############# KNN to get weights of branches ###########

def distance(dna1, dna2, expIndex):
    newDna1 = dna1[expIndex*4:(expIndex+1)*4]
    newDna2 = dna2[expIndex*4:(expIndex+1)*4]
    total = 0
    for index in range(len(newDna1)):
        total += ord(newDna1[index]) - ord(newDna2[index])
    return abs(total) 

def getNeighbors(trainingSet, testInstance, k, expIndex):
    distances = []
    testDNA = testInstance[0]
    for trainingInstance in trainingSet:
        curDNA = trainingInstance[0]
        dist = distance(testDNA, curDNA, expIndex)
        distances.append([dist, trainingInstance])
    distances.sort()
    neighbors = []
    for index in range(k):
        neighbors.append(distances[index][1])
    return neighbors

def reverseSort(votes):
    return sorted(votes)[::-1]

def sortVotes(typeVotes):
    votes = []
    for key in typeVotes:
        votes.append([typeVotes[key], key])
    votes = reverseSort(votes)
    return votes[0]

def getLabel(neighbors, curExpert):
    typeVotes = {}
    for neighbor in neighbors:
        curNeighbor = neighbor[2][curExpert]
        typeVotes[curNeighbor] = typeVotes.get(curNeighbor, 0) + 1
    typeVotes = sortVotes(typeVotes)
    return typeVotes[1]

def knnMain(trainingSet, testSet, experts, probs):
    k = 3
    for testInstance in testSet: 
        typeVotes = {}
        for expIndex, curExpert in enumerate(experts):
            neighbors = getNeighbors(trainingSet, testInstance, k, expIndex)
            label = getLabel(neighbors, curExpert)
            curProbs = probs[curExpert][label]
            curLD = "live" if curProbs >= .5 else "die"
            actualOutcome = testInstance[1]
            if (curLD != actualOutcome):
                experts[curExpert] /= 2
            else:
                pass
    return experts

experts = {"Speed": 1, "Height": 1, "Weight": 1}

newExperts = knnMain(trainingSet, testSet, experts, probs)

print(newExperts)


