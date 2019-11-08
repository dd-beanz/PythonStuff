def SelectionSort(arr):

  for startIndex in range(0,len(arr)):

    minVal = arr[startIndex]
    minIndex = startIndex
    
    for e in range(startIndex, len(arr)):
      
      if arr[e] < minVal:
        minVal = arr[e]
        minIndex = e 
    
    #Silly little tuple swap 
    arr[startIndex], arr[minIndex] = arr[minIndex], arr[startIndex]
  return arr

print(SelectionSort([5,4,3,2,1,0]))