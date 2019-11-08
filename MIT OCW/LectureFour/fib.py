#PERFORMS A FUNCTION THAT FINDS A FIBONACCI SEQUENCE FOR A GIVEN INTEGER
#THIS SOURCE CODE IS ASSOCIATED WITH CHAPTER 4.4 OF INTRO TO COMPSCI USING PYTHON
#GENERAL IDEAS OF THIS FILE RELATE TO GLOBAL VARIABLES IN REGARDS TO SCOPED FUNCTIONS

def fib(x):
  """
  Given an input of int x >= 0

  function will output the count of a fibonacci sequence
  """

  global fibCount #fibCount becomes a global variable that any scope/environment can acess
  
  fibCount += 1
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)
  
def testFib(n):
  for i in range(n+1):
    global fibCount
    fibCount = 0 #Starts the fibcount global off at zero and increments when the fib function is ran during next instruction
    print('fib of ', i, ' = ', fib(i))
    print('fib called: ', fibCount, ' times.')

testFib(6)
    