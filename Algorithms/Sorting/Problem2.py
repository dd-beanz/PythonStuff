def inputNames():
  '''
  Function takes in an input of 20 names and outputs an array of names 
  input; User input - no parameters needed
  output; nameArr - list of user names
  '''
  nameArr = []
  for _ in range(20):
    nameArr.append(str(input('Please enter a name: ')))
  
  return nameArr

def sortNames(arr):
  for index in range(len(arr)):
    minVal = arr[index]
    swapIndex = index

    for arrVal in range(index, len(arr)):
      if arr[arrVal] < minVal:
        minVal = arr[arrVal]
        swapIndex = arrVal

    arr[swapIndex] = arr[index]
    arr[index] = minVal
  return arr

print(sortNames(inputNames()))
