from random import *

lifeOutcomes = ['live', 'die']
descriptions = ['Speed', 'Height', 'Weight']

data = [] # All data stored in here

for i in range(500): # Num of total people test and training 
    newData = []

    # Random DNA string made with random letters
    curDNA = ''
    for i in range(len(descriptions)*4): 
        curDNA = curDNA + chr(randint(65,90))
    newData.append(curDNA)

    # Random life outcome, choice returns a random element in the list
    newData.append(choice(lifeOutcomes))

    # Add the new person to the list of people
    data.append(newData)

print(data)