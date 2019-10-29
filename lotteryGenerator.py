import random

def generateNumbers():
  lotteryArray = []
  for i in range(7):
    lotteryArray.append(random.randint(0,9))
  return lotteryArray

def displayNumbers(arr):
  for e in range(len(arr)):
    print(arr[e], end=' ')
  

displayNumbers(generateNumbers())
