def consecutiveNumbersInArray(array):

  index = 0
  consecCtr = 1
  consecNumDict = {}

  while index < len(array) - 1:

    if array[index] == array[index + 1]:
      consecCtr += 1
    else:
      consecCtr = 1

    if consecNumDict.get(array[index]) is None:
      consecNumDict[array[index]] = consecCtr
    elif consecNumDict.get(array[index]) is not None and consecCtr > consecNumDict[array[index]]:
      consecNumDict[array[index]] = consecCtr

    index += 1

  return consecNumDict

if __name__ == "__main__":
  testArray = [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0]
  testArray = [1, 2, 3, 4, 5, 6, 1, 1, 2, 43, 1, 43, 1, 1, 1, 0, 0, 0]
  print consecutiveNumbersInArray(testArray)
