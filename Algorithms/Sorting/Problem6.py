def inputUserAndNum():
  done = False
  name = []
  number = []

  while not done:
    name.append(str(input('Please enter a name: ')))
    number.append(str(input('Please enter a phone number: ')))

    doneInput = str(input('Are you complete? (y or n): '))
    
    if doneInput == 'y':
      done = True
  
  return (name, number)



def sortParallelArrays(arr1,arr2):
  for index in range(1,len(arr1)):
    key = arr1[index]
    key2 = arr2[index]
    val = index - 1

    while index > 0 and arr1[val] > key:
      arr1[val + 1] = arr1[val]
      arr2[val + 1] = arr2[val]

      arr1[val] = key
      arr2[val] = key2

      index -= 1
      val -= 1

  return (arr1,arr2)

def binarySearch(name, arr):
  low = 0
  high = len(arr)
  mid = (low+high) // 2
  while arr[mid] != name:
    if arr[mid] > name:
      high = mid
      mid = (high + low) // 2
    if arr[mid] < name:
      low = mid
      mid = (high + low) // 2
    if arr[mid] == name:
      return mid


(name, num) = inputUserAndNum()
(name, num) = sortParallelArrays(name,num)
searchTerm = str(input('Please enter a name for the search: '))

index = binarySearch(searchTerm,name)

print(name[index] + '\'s phone number is ' + num[index])



