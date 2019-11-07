def search(arr, n, x):
    for i in range(n):
    # Return the index of the element if the element
    # is found
        if (arr[i] == x):
            return i
    # return -1 if the element is not found
    return -1

