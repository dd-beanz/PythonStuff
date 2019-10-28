## Recursion -
#  **Process of repeating items in a self-similar way
#  '''Droste effect''' - picture within a picture
#  Divide and conquer 
#  Decrease and conquer 
# Algorithmically we reduce a problem into smaller parts in 
#order to solve problems 
# Semantically it is a function that is called within the body 
#of the function

def recursionOne(x):
  x -= 1
  if x == 1:
    print('Done!')
    return x
  else:
    recursionOne(x)
    print(x)
  
#recursionOne(5)

##Recursive reduction 
# a * a == a + a + a..... + a
# for recursion this is a + a * (b - 1)

def mult(a,b):
  if b == 1:
    return a
  else:
    return a + mult(a, b -1)

#print(mult(3,4))

def factorial(n):
  if n == 1:
    return 1
  else:
    print(n)
    return n * factorial(n-1)

#print(factorial(5))

#when writing recursive code once we hit the base case think
#of the function back tracking and performing the return sequences 
#backwards 

##MATHEMATICAL INDUCTION
#If I want to prove a statement is true on all integers 
#I prove it is true for the smallest value of n and 'n+1'

def fib(x):

  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x - 1) + fib(x - 2)
print(fib(5))

def isPalindrome(s):
  def toChars(s):
    s = s.lower()
    ans = ''
    for c in s:
      if c in 'abcdefghijklmnopqrstuvwxyz':
        ans = ans + c
    return ans

  def isPal(s):
    if len(s) <= 1:
      return True
    else:
      return s[0] == s[-1] and isPal(s[1:-1])
  return isPal(toChars(s))

###############################################
#Dictionary data-type 
#way to store data in a key:value pair 

grades = {'Devan': ['A', 6.001], 'Carl': ['B',2.001]}

print(grades)

for e in grades.values():
  print(e)


def lyricFrequencies(lyrics):
  myDict = {}
  for word in lyrics:
    if word in myDict:
      myDict[word] += 1
    else:
      myDict[word] = 1
  
#####CHAPTER 4.3 IN ICS#####
#Recursion is made up of two parts a base case that specifies the result 
#for a special case and a recursive (inductive) case  

#A classic Inductive definition : 
#     1! = 1 <---- base case 
#   (n + 1)! = (n + 1) * n!

# Due to when you are back tracking in recursion we need to have the base case as the first possible 
#return value and work towards it, so in factorial so n is going to be multiplied by n - 1 during each turn

#Lets do a factorial recursion
def factorialICS(n):
  if n == 1:
    return 1
  else:
    return n * factorialICS(n - 1)

#print(factorialICS(n=20))

#Basic summation recursion - adds from n to 1 

def summation(n):
  if n == 1:
    return 1
  else:
    return n + summation(n - 1)

print(summation(10))
