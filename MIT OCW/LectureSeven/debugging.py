try:
  a = int(input('Please enter a number'))
  b = int(input('Please enter a second number'))
  print(a/b)

except ValueError:
  print('Bug in user input.')
except ZeroDivisionError:
  print('Cannot divide by zero')
except:
  print('Something went wrong')
  