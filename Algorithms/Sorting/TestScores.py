import BubbleSort

def testScoreInput():
  testScores = []
  flagged = True
  while flagged:
    score = input('Please input test scores (exit if you are finished with input): ')
    if score == 'exit':
      flagged = False
    else:
      testScores.append(float(score))
  return testScores

scores = testScoreInput()

print('========================')
print('SORTED TEST SCORES')
print(BubbleSort.BubbleSort(scores))


