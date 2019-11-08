#FUNCTIONS, ABSTRACTION, and DECOMPOSITION

def isEven(n):
  """
  Input: n, a positive int
  Outputs True is n is even, otherwise False
  """
  print('Variable input is even: ')
  return n%2 == 0

  #When above return value is True the body is returned if false it does not get returned 

isEven(3)

def f(x):
  x = x + 1 
  print('in f(x) : x = ', x)
  return x

for i in range(20):
  if isEven(i):
    print(i, 'Even')
  else:
    print(i, 'Odd')

def funcA():
  print('inside func a')
def functB(z):
  print('inside func b')
  return z()

functB(funcA)

def mult(x,y):
  print(x*y)

print(mult(2,3))
mult(2,3)