#Program for testing a bisection root finding function

#THIS PROGRAM FILE IS ASSOCIATED WITH CHAPTER 4.2 IN INTRO TO COMPSCI USING PYTHON
#THIS CHAPTER DESCRIBES FUNCTION SPECIFICATIONS IN USE WITH THE DOCSTRING HELP AND TEST FUNCTION IDEAS

def findRoot(x,power,epsilon):
  """
  Input : x , power , epsilon
          epsilon > 0 and power >= 1
          Returns float y such that y**power is withink epsilon of x

  Usage : program will take an input x power and epsilon
  """

  if x < 0 and power%2 == 0:
    return None
  
  high = max(1.0, x)
  low = min(-1.0, x)
  ans = (high+low)/2.0

  while abs(ans**power - x) >= epsilon:
    if ans ** power < x:
      low = ans
    else:
      high = ans
    ans = (high + low)/2.0
  return ans

def testRoot():
  epsilon = 0.01
  for x in [24,4,9]:
    for power in [2,3,4]:
      print('Testing: ', x)
      print('Testing power: ', power)

      result = findRoot(x,power,epsilon)

      if result == None:
        print('Cannot find root')
      else:
        print('Root: ', x**power, ' ~= ', result)

testRoot()
#print(findRoot(4,2,1))
help(findRoot)