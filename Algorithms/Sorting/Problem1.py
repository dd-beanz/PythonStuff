#Sorting golf scores 
def obtainInput():
  print('Please enter 10 golf scores')
  arr = []
  for i in range(10):
    arr.append(int(input('Please enter a score: ')))
  
  return arr

def sortScores(arr):
  for index in range(1,len(arr)):
    arrVal = arr[index]
    i = index - 1

    while index > 0 and arr[i] > arrVal:
      arr[i + 1] = arr[i]
      i -= 1
      index -= 1
    
    arr[index] = arrVal
  return arr


print(sortScores(obtainInput()))