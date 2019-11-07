import random

def distance(point1, point2):
    dx = (point1[0] - point2[0])**2
    dy = (point1[1] - point2[1])**2
    return (dx+dy)**.5

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    for trainingInstance in trainingSet:
        dist = distance(testInstance, trainingInstance)
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

def getLabel(neighbors):
    typeVotes = {}
    for neighbor in neighbors:
        curNeighbor = neighbor[-1]
        typeVotes[curNeighbor] = typeVotes.get(curNeighbor, 0) + 1
    typeVotes = sortVotes(typeVotes)
    return typeVotes[1]


def main(trainingSet, testSet):
    k = 3
    for testInstance in testSet: #currently just does one in test Set
        neighbors = getNeighbors(trainingSet, testInstance, k)
        label = getLabel(neighbors)
        return label

def getDataFromFile(filename):
    with open(filename, 'r') as f:
        data = eval(f.read()) # NOTE: DO NOT USE eval unless you are absolutely
                              # sure that your file is uncorruptable!!!
    return data


trainingSet = getDataFromFile("foo.txt")

for i in contentsRead:
   print(i)


lifeOutcomes = ['live', 'die']
choices = {'Speed': ['Fast', 'Medium', 'Slow'],
            'Height': ['Tall', 'Medium', 'Smaller than a breadbox'],
            'Weight': ['10lbs', '100lbs', '1000lbs'],
            'Sight': ['Ultraviolet', 'Human visible light','My future fading into oblivion'],
            'Touch': ['Pressure', 'Temperature', 'Pressure:Temperature'],
            'Hairiness': ['Covered', 'Partially Covered', 'Bare'],
            'Taste': ['Sweet', 'Salty', 'Savory', 'Sweet:Salty:Savory'],
            'Smell': ['Fruity', 'Chemical', 'Pungent', 'Fruity:Chemical:Pungent'],
            'Fingers': ['3', '5', '7'],
            'Legs:Arms': ['2', '4', '6'],
            'Brain Size': ['Large', 'Medium', 'Small'],
            'Brain Size': ['Large', 'Medium', 'Small'],
            'Emotion': ['Introvert', 'Extrovert', "Aware of one's own existence, Introverted Extrovert"]
            }

data = []
for i in range(200):
    newData = []
    dictOfChar = {}
    lifeOutcome = ''
    curSet = ''
    for i in range(len(choices)*4): # 4 DNA Pieces per chart
        curSet = curSet + chr(random.randint(65,90))
    newData.append(curSet)
    lifeOutcome = random.choice(lifeOutcomes)
    newData.append(lifeOutcome)
    for key in choices:
        dictOfChar[key] = random.choice(choices[key])
    index = 0
    for key in dictOfChar: # Current Method 
        newWord = curSet[index*4:(index*4)+4] # Using 4 DNA pieces per chart
        index += 1
        x0 = 0
        lastLetter = ''
        for c in newWord:
            x0 += ord(c) 
            lastLetter = c
        x0 = random.randint(x0-2*ord(lastLetter), x0+2*ord(lastLetter)) # Current function
        y0 = random.randint(0, x0) # Current Function
        dictOfChar[key] = [x0, y0, lifeOutcome, dictOfChar[key]] 
    newData.append(dictOfChar)
    data.append(newData)

#print(data)
















