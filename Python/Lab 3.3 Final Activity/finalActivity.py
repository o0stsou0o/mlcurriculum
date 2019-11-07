#!/usr/bin/env python3
################################################################################
# DO NOT MODIFY THIS PART OF THE FILE
#
# (Unless you are sure of what you are doing :P )
################################################################################

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
                str(self.__incomeOver50K__))

    def __repr__(self):
        return ("Person("+str(self.age) + ", " + repr(self.workclass) + ", " + repr(self.education) +
                ", " + repr(self.maritalStatus) + ", " + repr(self.occupation) + ", " +
                repr(self.race) + ", " + repr(self.sex) + ", " + str(self.capitalIncome) + ", " +
                str(self.hoursPerWeek) + ", " + repr(self.nativeCountry) + ", " +
                str(self.__incomeOver50K__) + ")")

class Database(object):
    def __init__(self):
        self.database = []
        filepath = "adultTrainingData.csv"
        with open(filepath, 'rb') as csvfile:
            fileReader = csv.reader(csvfile)
            for row in fileReader:
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

    def __getitem__(self, key):
        return self.database[key]

    def __len__(self):
        return len(self.database)

################################################################################
# WRITE YOUR CODE BELOW THIS
################################################################################

# First, load the database
database = Database()

# This function will take in a person (an instance of the Person class) and
# should return a boolean that indicates whether you predict that person has
# an income >50K (True) or <=50K (False). Use any data analysis or machine
# learning techniques that you would like. Feel free to write helper functions
# or to write separate code to get parameters that are then hardcoded into
# this function (like you did with decision trees)
#
# I should be able to copy and paste this function (and necessary helper
# functions) into my computer and have it work.
#
# Note that for any global variables you use, including function names, please
# add your name at the end of the variable so it won't conflict with other
# student's variable names. For example, if my name is "Amal", my main function
# should be called "predictIncomeAmal".
#
# This function should also not use "database". Rather, database should be used
# to calculate parameters that you then use in the "predictIncome" function.
def predictIncome(person):
    return False
