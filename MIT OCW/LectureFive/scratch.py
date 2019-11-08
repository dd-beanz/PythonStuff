a = ((200,'a'),(500,'b'),(100,'a'))

def getTupleData(tuple):
  words = ()
  nums = ()
  for t in tuple:
    nums = nums + (t[0],)
    if t[1] not in words:
      words = words + (t[1],)

  min_n = min(nums)
  max_n = max(nums)
  unique_words = len(words)

  return (min_n, max_n, unique_words, words, nums)

(mi,mx,uw,w,n) = getTupleData(a)

print(mi)
print(mx)
print(uw)
print(w)
print(n)
