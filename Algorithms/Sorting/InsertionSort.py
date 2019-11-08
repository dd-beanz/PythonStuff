def InsertionSort(arr):
  for index in range(1,len(arr)):
    arrVal = arr[index]
    i = index - 1

    while index > 0 and arr[i] > arrVal:
      arr[i + 1] = arr[i]
      i -= 1
    
    arr[i + 1] = arrVal
  return arr


print(InsertionSort([1,6,3,7,9,2]))
