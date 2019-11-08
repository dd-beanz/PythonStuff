def inputRain():
  arr = []
  for i in range(12):
    arr.append(float(input('Please enter month '+str(i)+' rainfall: ')))
  return arr

def calculateRainFall(arr):
  arr = sorted(arr)
  total = 0
  average = 0

  for e in arr:
    total += e
  average = total/12
  print('Total rainfall: %f', total)
  print('Average montly rainfall: %f', average)
  print('Most amount of rainfall %f', arr[-1])
  print('Least amount of rainfall: %f', arr[0])
  return 0  

calculateRainFall(inputRain())