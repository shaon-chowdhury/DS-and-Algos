def findSubarrayWithLowestSum(array, size):

  index = size
  minRunningSum = sum(array[index-size:index])
  minIndex = index-size
  maxIndex = size

  while index < len(array):
    runningSum = sum(array[index-size:index])
    if runningSum < minRunningSum:
      minRunningSum = runningSum
      minIndex = index-size
      maxIndex = index
    runningSum -= array[index-size]
    runningSum += array[size + 1]
    index += 1

  return array[minIndex:maxIndex]

if __name__ == "__main__":
    testArray = [1, 2, 1, 3, 1, 1, 1, 4, 2, 3]
    testArray = [5, 0, 23, 41, 1, 23, 53, 2, 1]
    testArray = [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0]
    print findSubarrayWithLowestSum(testArray, 3)
