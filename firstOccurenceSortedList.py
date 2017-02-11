def binarySearch(array, searchVal):

    low = 0
    high = len(array) - 1
    result = -1

    while low <= high:
        mid = (low + high)/2
        if searchVal == array[mid]:
            result = mid
            high = mid - 1
        elif searchVal < array[mid]:
            high = mid - 1
        elif searchVal > array[mid]:
            low = mid + 1
        else:
            return -1

    return result

if __name__ == "__main__":

    testArray = range(8) #-1
    testArray = [1, 2, 8, 8, 8, 23, 44] #2
    print binarySearch(testArray, 8)
