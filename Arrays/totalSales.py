def weekSales():
  arr = []
  for i in range(7):
    arr.append(float(input('Please enter day '+str(i+1)+' sales:')))
  
  return arr

def calculateTotal(arr):
  total = 0
  for i in arr:
    total += i
  return total

print(calculateTotal(weekSales()))
