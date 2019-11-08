#Define max value via our own function
def maxVal(x,y):
  if x > y:
    return x
  else:
    return y

## X and Y are formal parameters 
## def tells python we are about to define a function

z = maxVal(12,8)*maxVal(2,4)

###print(z)

def printName(first,last,reverse):
  if reverse:
    print(last + ' ' + first )
  else:
    print(first + ' ' + last)

def f(x): #x used as formal parameter 
  def g():
    x = 'abc'
    print(x)
  def h():
    z = x
    print('z = ', z)
  x = x + 1
  print('x = ', x)
  h()
  g()
  print('x = ', x)
  return g

x = 3
y = 2

z = f(x)

print('z = ', z)
print('y = ', y)
print('x = ', x)

for x in [23,22,10,7]:
  print(x)