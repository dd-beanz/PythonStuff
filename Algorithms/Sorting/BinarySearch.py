#Binary search algorithm, takes a sorted array of elements and searches for a given value starting at the half the array.... n1 + n2 / 2

def BinarySort(n,arr):
  lower = 0
  upper = len(arr)
  middle = abs((lower + upper) // 2 )
  steps = 0

  if n == arr[middle]:
    return 'Found!'
  
  while n != arr[middle] and middle <= upper:
    steps += 1
    if n > arr[middle]:  
      lower = middle
      middle = abs((lower + upper) // 2)
    if n < arr[middle]:
      upper = middle
      middle = (lower + upper) // 2
    if n == arr[middle]:
      print('Step count:', steps)
      return 'Found!'
  return 'Cannot find'
  


print(BinarySort(3,[1,2,3,4,5,6,7,8,9,10,11]))

