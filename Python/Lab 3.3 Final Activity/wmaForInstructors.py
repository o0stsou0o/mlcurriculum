#!/usr/bin/env python3
import matplotlib.pyplot as plt

import csv

class Person(object):
    def __init__(self, age, workclass, education, maritalStatus, occupation,
                 race, sex, capitalIncome, hoursPerWeek,
                 nativeCountry, incomeOver50K):
        self.age = age
        self.workclass = workclass
        self.education = education
        self.maritalStatus = maritalStatus
        self.occupation = occupation
        self.race = race
        self.sex = sex
        self.capitalIncome = capitalIncome
        self.hoursPerWeek = hoursPerWeek
        self.nativeCountry = nativeCountry
        self.__incomeOver50K__ = incomeOver50K

    def __str__(self):
        return (str(self.age) + ", " + self.workclass + ", " + self.education +
                ", " + self.maritalStatus + ", " + self.occupation + ", " +
                self.race + ", " + self.sex + ", " + str(self.capitalIncome) + ", " +
                str(self.hoursPerWeek) + ", " + self.nativeCountry + ", " +
                str(self.incomeOver50K))

    def __repr__(self):
        return ("Person("+str(self.age) + ", " + repr(self.workclass) + ", " + repr(self.education) +
                ", " + repr(self.maritalStatus) + ", " + repr(self.occupation) + ", " +
                repr(self.race) + ", " + repr(self.sex) + ", " + str(self.capitalIncome) + ", " +
                str(self.hoursPerWeek) + ", " + repr(self.nativeCountry) + ", " +
                str(self.incomeOver50K) + ")")

class Database(object):
    def __init__(self):
        self.database = []
        filepath = "adultTestData.csv"
        with open(filepath, 'rb') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                if len(row) < 14: break
                # Eliminate all data points with missing values from the dataset
                foundUnknown = False
                for data in row:
                    if '?' in data:
                        foundUnknown = True
                        continue
                if foundUnknown: continue
                # Convert the entries to standard python data types
                age = int(row[0])
                workclass = row[1].strip()
                education = row[3].strip()
                maritalStatus = row[5].strip()
                occupation = row[6].strip()
                race = row[8].strip()
                sex = row[9].strip()
                capitalGain = int(row[10].strip())
                capitalLoss = int(row[11].strip())
                capitalIncome = capitalGain - capitalLoss
                hoursPerWeek = int(row[12].strip())
                nativeCountry = row[13].strip()
                incomeOver50K = True if ">50K" in row[14] else False
                self.database.append(Person(age, workclass, education,
                    maritalStatus, occupation, race, sex, capitalIncome,
                    hoursPerWeek, nativeCountry, incomeOver50K))
            print("Loaded Database!")

    def __iter__(self):
        return iter(self.database)

def alwaysTrue(person): return True
def alwaysFalse(person): return False

# Initialize all variables
experts = [alwaysTrue, alwaysFalse] # these should all be uniquely named student functions
expertWeights = [1.0 for expert in experts]
predictionLosses = []
expertLosses = [[] for expert in experts]
penalty = 0.99
database = Database()

for person in database:
    # print(person)
    expertPredictions = []
    trueWeight = 0.0
    falseWeight = 0.0

    for expertI in range(len(experts)):
        expert = experts[expertI]
        prediction = expert(person)
        expertPredictions.append(prediction)
        if prediction: trueWeight += expertWeights[expertI]
        else: falseWeight += expertWeights[expertI]
        # print(prediction)


    prediction = trueWeight > falseWeight
    actual = person.__incomeOver50K__
    # print(prediction, actual)


    if prediction != actual:
        predictionLosses.append(1.0)
    else:
        predictionLosses.append(0.0)

    for expertI in range(len(experts)):
        expertPrediction = expertPredictions[expertI]
        if expertPrediction != actual:
            expertWeights[expertI] *= penalty
            expertLosses[expertI].append(1.0)
        else:
            expertLosses[expertI].append(0.0)
    print(expertWeights)

for expertI in range(len(experts)):
    print(str(experts[expertI]), expertWeights[expertI])

# Convert Loss to Cumulative Loss
predictionCumulativeLoss = [0.0]
for loss in predictionLosses:
    predictionCumulativeLoss.append(predictionCumulativeLoss[-1] + loss)
expertCumulativeLosses = [[0.0] for expert in experts]
for expertI in range(len(experts)):
    expertLoss = expertLosses[expertI]
    for loss in expertLoss:
        expertCumulativeLosses[expertI].append(expertCumulativeLosses[expertI][-1] + loss)

# Convert Cumulative Loss to Average Cumulative Loss
predictionAverageCumulativeLoss = [predictionCumulativeLoss[t+1]/(t+1) for t in range(len(predictionCumulativeLoss)-1)]
expertAverageCumulativeLosses = [[expertCumulativeLosses[expertI][t+1]/(t+1) for t in range(len(expertCumulativeLosses[expertI])-1)] for expertI in range(len(experts))]

# Plot the Cumulative Losses
fig, ax = plt.subplots()
ax.set_title("Cumulative Loss for Experts")
expertColors = ["red", "orange", "yellow", "green", "turquoise", "purple", "pink", "indigo", "brown", "black", "grey"]
for expertI in range(len(experts)):
    color = expertColors[expertI]
    label = experts[expertI].__name__
    expertAverageCumulativeLoss = expertAverageCumulativeLosses[expertI]
    ax.plot(range(1, len(expertAverageCumulativeLoss)+1), expertAverageCumulativeLoss, color=color, label=label)
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
