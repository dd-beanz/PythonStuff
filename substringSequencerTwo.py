def solution(s):
    if len(s)%2==0:
        for i in range(len(s)):
          print(s[0:len(s)//(2*(i+1))])
          print('\n')
          print(s[len(s)//(2*(i+1)):])
    
    
string = 'abccbaabccba'

solution(string)