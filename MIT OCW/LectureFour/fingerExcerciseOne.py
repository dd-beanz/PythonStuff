#Finger exercise chapter four : functions 
#finger exercise one

def isIn(string1,string2):
  """
  Input ; string1 - string literal
        ; string2 - string literal
  Output; True if string1 in string2
        ; True if string2 in string1
        ; False if not 
  """

  if string1 in string2 or string2 in string1:
    return True
  else:
    return False

print(isIn('hello world!', 'hello'))