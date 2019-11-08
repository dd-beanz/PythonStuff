x = 4
y = 7
z = 13

if x%2 == 0 and y%2 == 0 and z%2 == 0:
  print('No numbers are odd.')
else:
  if x > y and x%2 != 0:
    print(x)
  if y > z and y%2 != 0:
    print(y)
  elif z%2 != 0:
    print(z)