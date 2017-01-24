def minMaxSubarray(array):

  maxSubarraySize = len(array)
  maxEle = max(array)
  minEle = min(array)
  lastMinEle = -1
  lastMaxEle = -1
  index = 0

  while index < len(array):

    if array[index] == minEle:
      lastMinEle = index
    if array[index] == maxEle:
      lastMaxEle = index

    print lastMaxEle, lastMinEle, maxSubarraySize

    if lastMaxEle != -1 and lastMinEle != -1:
        maxSubarraySize = min(abs(lastMaxEle - lastMinEle) + 1, maxSubarraySize)

    index += 1

  return maxSubarraySize

if __name__ == "__main__":
    testArray = [1, 5, 9, 7, 1, 9, 4]
    testArray = [5, 5, 5 ,5]
    testArray = [55, 23, 99, 10, 23, 99, 7, 55, 5, 1, 2]
    print minMaxSubarray(testArray)
