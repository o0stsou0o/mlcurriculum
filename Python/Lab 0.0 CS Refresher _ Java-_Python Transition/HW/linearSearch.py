# Takes in a list l (can be sorted or unsorted) and an elem, and searches the
# list for elem using linear search. If elem is in the list, it returns the
# index of elem. If not, it returns -1.
def findLinearSearch(l, elem):
    # Iterate over all the indices in the list
    for i in range(len(l)):
    # Return the index of the element if the element
    # is found
        if (l[i] == elem):
            return i
    # return -1 if the element is not found
    return -1
