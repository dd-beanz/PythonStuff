def intersect(t1,t2):
  '''
  Detects similar elements given two tuples
  '''
  result = ()
  for e in t1:
    if e in t2:
      result += (e,)
  return result

a = ('a','b',1,2,3)
b = ('b',4,3,1)

print(intersect(a,b))

#SEQUENCES AND MULTIPLE ASSIGNMENT - This section showcases a function in which we 
#bind two integers ie. n1 and n2 and then using a for loop we loop over all numbers to find LCV
#after finding it we return a tuple

def findDivisors(n1,n2):
  '''
  assumes n1 and n2 are positive integers 
  returns a tuple containing the smallest common divisor > 1 and 
  the largest common divisor of n1 and n2. If no divisor returns None,None
  '''
  minVal, maxVal = (None,None)
  for i in range(2, min(n1,n2) + 1):
    if n1%i == 0 and n2%i == 0:
      if minVal == None:
        minVal = i
      maxVal = i
  return (minVal,maxVal)

#FUNCTIONS AS OBJECTS, functions can be passed as an argument for other functions
#this is called highorder function programming. Functions like objects can be used in lists, etc

def  applyToEach(L, f):
  '''
  Assumes that L is a list of elements, f is a function
  Mutates L by replacing each element, e, of L by f(e)
  '''
  for i in range(len(L)):
    L[i] = f(L[i])
  return L

#Lamba functions (anonymous functions) >>>> ' lambda <sequence of variable names>: <expression> '
#map is similar to the applyToEach function we proposed above. Map is built in
#LAMBDA'S ARE FREQUENTLY PASSED THROUGH HIGHER ORDER FUNCTIONS



L =[]
for i in map(lambda x,y: x**y, [1,2,3,4],[1,2,3,4]):
  L.append(i)
print(L)
