def binarySearch(arr, x):
    l = 0 
    r = len(arr) - 1
    while (l <= r):
        m = l + (r-l)//2
 
        # Check if x is present at mid
        if (arr[m] == x):
            return m
 
        # If x greater, ignore left half
        if (arr[m] < x):
            l = m + 1
 
        # If x is smaller, ignore right half
        else:
            r = m - 1
 
    # if we reach here, then element was not present
    return -1;
 
arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = binarySearch(arr, x)
if (result == -1):
    print("Element not present")
else:
    print("Element found at index "+str(result))
