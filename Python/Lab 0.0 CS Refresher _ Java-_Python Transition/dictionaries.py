d = { "cow":5, "dog":98, "cat":1 }
print(d)    # ditto!
print("___________")

ages = dict()
key = "fred"
value = 38
ages[key] = value  # "fred" is the key, 38 is the value
print(ages[key])
print("___________")

d = dict()
# d[key] = value
d[2] = 100 # No key present, so it adds the key:value to the dictionary
d[4] = 200
d[8] = 300
print(d)  # unpredictable order
print("___________")

d = { 1:"a", 2:"b" }
for key, value in d.items():
   print(key, value)

# another option just know that it exists
#for key in d:
 #  print(key, d[key])
print("___________")

d = { 1:"a", 2:"b" }
print(0 in d)
print(1 in d)
print("a" in d) # surprised?
print("___________")

d = { 1:"a", 2:"b" }
print(d[1])
d[1] = 42
print(d[1])
print("___________")

d = { 1:"a", 2:"b" }
print(d.get(1))     # works like d[1] here
print(d.get(1, 42)) # default is ignored
print(d.get(0))     # doesn't crash!
print(d.get(0, 42)) # default is used
print("___________")


d = {0: "dog", 1: "cat"}
d[2] = "mouse" # will add a new key:value pair if the value is not currently
               # in the dictionary
print(d)
print("___________")


# comprehension
# This:
d1 = {i : True for i in range(5)}

# Is equivalent to this:
d2 = dict()
for i in range(5):
    d2[i] = True
print("d1 = ", d1)
print("d2 = ", d2)
print("___________")
