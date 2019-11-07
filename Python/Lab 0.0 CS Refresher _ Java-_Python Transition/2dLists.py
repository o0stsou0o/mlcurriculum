# Examples from the 15-112 website

# Creating
def make2dList(rows, cols):
    a=[]
    for row in range(rows): a += [[0]*cols]
    return a

rows = 3
cols = 2

a = make2dList(rows, cols)
print(a)
print("--------------------------")


a = [ [ 2, 3, 4 ] , [ 5, 6, 7 ] ]
print(a)
a.append(["another list"])
print(a)
print("--------------------------")

# Creating: List comprehension
rows = 3
cols = 2

a = [ ([0] * cols) for row in range(rows) ]

print("   a =", a)
print("--------------------------")

# Indexing

a = [ [ 2, 3, 4 ] , [ 5, 6, 7 ] ]
print(a[0])
print(a[1])
# print(a[2]) this will crash
print(a[0][0])
print(a[0][1])
print(a[0][2])
# print(a[0][3]) this will crash
print("--------------------------")


# Create an "arbitrary" 2d List
a = [ [ 2, 3, 5] , [ 1, 4, 7 ] ]
print("Before: a =", a)

# Now find its dimensions
rows = len(a)
cols = len(a[0])

# And now loop over every element
# Here, we'll add one to each element,
# just to make a change we can easily see
for row in range(rows):
    for col in range(cols):
        # This code will be run rows*cols times, once for each
        # element in the 2d list
        a[row][col] += 1

# Finally, print the results
print("After:  a =", a)
print("--------------------------")


