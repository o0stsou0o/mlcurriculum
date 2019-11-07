from random import *

lifeOutcomes = ['live', 'die']
descriptions = {'Speed': ['Fast', 'Medium', 'Slow'],
            'Height': ['Tall', 'Average', 'Smaller than a breadbox'],
            'Weight': ['10lbs', '100lbs', '1000lbs'],
        }

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

    # Random characteristics from above
    characteristics = {}
    for types in descriptions:
        characteristics[types] = choice(descriptions[types])
    newData.append(characteristics)

    # Add the new person to the list of people
    data.append(newData)

print(data)