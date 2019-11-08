def sortChargeNumbers():
  verification = [5658845, 4520125, 7895122, 8777541, 8451277, 1302850,
                  8080152, 4562555, 5552012, 5050552, 7825877, 1250255,
                  1005231, 6545231, 3852085, 7576651, 7881200, 4581002] 

  for index in range(1,len(verification)):
    key = verification[index]
    startVal = index - 1

    while index > 0 and verification[startVal] > key:
      verification[startVal + 1] = verification[startVal]
      verification[startVal] = key
      startVal -= 1
      index -= 1
    
  return verification

def chargeNumberBinarySearch(arr,n):
  high = len(arr)
  low = 0
  mid = (high + low) // 2
  
  while n != arr[mid]:
    if arr[mid] < n:
      low = mid
      mid = (high + low) // 2
    if arr[mid] > n:
      high = mid
      mid = (high + low) // 2
    if arr[mid] == n:
      print('Found:',n,'Index:',mid)
      return 0
    if mid == 0 or mid == len(arr) - 1:
      print('Number not found.')
      return 0

chargeNumberBinarySearch(sortChargeNumbers(),int(input('Please enter charge number: ')))