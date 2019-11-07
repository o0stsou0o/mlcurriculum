a = [ "hello" ]
b = [ 42 ]

print(type(a), len(a), a)
print(type(b), len(b), b)
print(a == b)

print("________________")

def f(a):
    a[0] = 42
a = [2, 3, 5, 7]
f(a)
print(a)

print("________________")

a = [ 2, 3, 5, 2, 6, 2, 2, 7 ]
print("a      =", a)
print("2 in a =", (2 in a))

print("________________")

a = [ 2, 3 ]
a.append(7)
print(a)
print("________________")


a = [ 2, 3, 4, 5, 6, 7, 8 ]
print("a =", a)
item = a.pop(3)
print("After item = a.pop(3)")
print("   item =", item)
print("   a =", a)
print("________________")

a = [ 7, 2, 5, 3, 5, 11, 7 ]
print("At first, a =", a)
a.sort()
print("After a.sort(), a =",a)
print("________________")


# Create an "arbitrary" 2d List
a = [ [ 2, 3, 5] , [ 1, 4, 7 ] ]
print("a = ", a)

# Now find its dimensions
rows = len(a)
cols = len(a[0])
print("rows =", rows)
print("cols =", cols)
print("________________")

# Comprehensions

# This:
a1 = [i for i in range(10)]
print("a1 = ", a1)

# Is equivalent to:
a2 = []
for i in range(10):
    a.append(i)
print("a2 = ", a2)

a = [(i*100) for i in range(20) if i%5 == 0]
print(a)
print("________________")


