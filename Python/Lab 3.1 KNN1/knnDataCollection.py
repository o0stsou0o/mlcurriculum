from random import *

data = [] # All data stored in here

for i in range(500): # Num of total stars to test and training 
    # Random Age
    age = uniform(1, 7)

    # Random Temperature
    hotness = uniform(96, 110)

    # Add some variation, so it isn't a hard cutoff
    chance = uniform(99, 101)

    # Add some chance of temperature variation, and state all stars less than 
    # 5 cannot superNova
    if (hotness > chance and age < 5):
        superNova = True
    else:
        superNova = False

    # Add the new star to the list of stars
    data.append([age, hotness, superNova])

print(data)
