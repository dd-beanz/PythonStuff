def rainfallInput():
  '''
  No parameters needed,
  Outputs an array of floating point numbers via user input for rainfall
  '''
  arr = []
  for _ in range(12):
    print('Please enter rainfall for month', _+1)
    arr.append(float(input()))
  return arr

def sortRainfall(arr):
  '''
  Parameters: arr - Array
  Takes in an array and outputs an Array
  Output: Sorted array (ascending)
  '''
  for index in range(1,len(arr)):
    key = arr[index]
    lastVal = index - 1

    while index > 0 and arr[lastVal] > key:
      arr[lastVal + 1] = arr[lastVal]
      arr[lastVal] = key
      index -= 1
      lastVal -= 1
  return arr

def calculateTotal(arr):
  total = 0
  for val in arr:
    total += val
  
  return total

def lowestHighest(arr):
  print('Lowest rainfall:', arr[0])
  print('Highest rainfall:', arr[-1])
  return 0

rainFall = sortRainfall(rainfallInput())

print('Sorted rainfall array -',rainFall)
print('Total rainfall -', calculateTotal(rainFall))
lowestHighest(rainFall)