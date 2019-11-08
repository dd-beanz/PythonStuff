def check(temp,s):
  inputStringLen = len(s)
  tempStringLen = len(temp)
  if inputStringLen%tempStringLen == 0:
    temp = temp * (len(s) // len(temp))
    if temp == s:
      return True
    else:
      return False
  else:
    return False

def solution(s):

  s = ''.join(s.split())

  if s.isalpha() == False:
    return 0
  
  temp = ''
  s = s.lower()

  for i in s:
    if i not in temp or i not in temp[0]:
      temp = temp + i
    elif i in temp[0]:
      if check(temp=temp,s=s) and s[-1] == temp[-1]:
        return len(s) / len(temp)
      else:
        temp = temp + i
  return 0
        

string = 'abcAdcabc232'

print(int(solution(string)))