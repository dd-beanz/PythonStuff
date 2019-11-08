hand = {'h':1,'n':1,'e':1,'*':1,'y':1}
word = 'h*ney'
wordList = 'honey'
VOWELS = ['a','e','i','o','u']
wordArr = []

wildCardLetter = word.find('*')

def valid_Word(word,wordList):
  if '*' in  word:
    for _ in word:
      wordArr.append(_)

    for letter in VOWELS:
      wordArr[wildCardLetter] = letter
      if ''.join(wordArr) in wordList:
        print(''.join(wordArr).replace(letter,''))
    return False

print(valid_Word(word,wordList))