# https://www.cs.cmu.edu/~112/notes/notes-strings.html
# All examples found here

# Indexing
s = "abcdefgh"
print(s)
print(s[0])
print(s[1])
print(s[2])

print("-----------")
print(s[len(s)-1])
#print(s[len(s)])  # crashes (string index out of range)

# Indexing over a range
s = "abcdefgh"
print(s)
print(s[0:3])
print(s[1:3])
print("-----------")

# Looping through a string
s = "abcd"
for c in s:
    print(c)

print("-----------")

s = "abcd"
for i in range(len(s)):
    print(i, s[i])

print("-----------")

# Strings are immutable
s = "abcde"
#s[2] = "z"  # Error! Cannot assign into s[i] Strings are immutable
print("-----------")

s = 'soon'
p = '--pop'
sp = s+p
print(sp+" 77spaghetti")
print("-----------")


s = '8'
i = int(8)
f = float(s)
s2 = str(i)
print(i, type(i))
print(f, type(f))
print(s2, type(s2))
print(s, type(s))
print("-----------")
