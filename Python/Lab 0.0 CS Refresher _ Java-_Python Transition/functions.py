# Examples from 112 Website

x = 5
def f(y, z):
    result = x + y + z
    return result
print(f(1, 2)) # 8
print(f(3, 4)) # 12
print("_______________")


def isPositive(x):
    return (x > 0)

print(isPositive(5))  # True
print("_______________")


def isPositive(x):
    return ("Hello")

print(isPositive(5))  # prints Hello
print("_______________")


g = 100
def f(x):
    # If we modify a global variable, we must declare it as global.
    # Otherwise, Python will assume it is a local variable.
    global g
    g += 1
    return x + g

print(f(5)) # 106
print(f(6)) # 108
print(g)    # 102
print("_______________")


#

# Tell students to create a function that uses a helper function that increases 
# every letters ord by one, if the letter is z it wraps around.
# Sample example
def getOrd(element):
    if element == 'z':
        return ord('a') - 1
    return ord(element)

def changeLetter(myList):
    curIndex = 0
    for element in myList:
        ordOfElement = getOrd(element)
        myList[curIndex] = str(chr(ordOfElement+1))
        curIndex += 1

myList = ["a", "b", "c", "d", "z"]
print(myList)
changeLetter(myList)
print(myList)



