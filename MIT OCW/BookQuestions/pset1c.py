#PART C: Finding the right amount to save away

starting_salary = float(input('Enter the starting salary: '))
#salary = 0

#Variable initilization
semi_annual_raise = 0.07
annual_return = 0.04
cost_of_home = 1000000
down_payment = cost_of_home * 0.25
high_epsilon = 100
low_epsilon = -100
high = 10000
low = 0
percent = (high + low)//2
bisection = 0

while True:
  salary = starting_salary 
  current_savings = 0
  month = 0
  
  #Iteration to add up savings per high + low /2 percent
  while month <= 36:
    month += 1
    if month % 6 == 0:
      salary = salary + (salary * semi_annual_raise)
    current_savings = current_savings + (salary/12)*(percent/10000) + (current_savings * annual_return)
    print(current_savings)
  if abs(current_savings - down_payment) <= high_epsilon:
    print('Best savings rate: ' + str(percent/10000))
    print('Steps in bisection: ' + str(bisection))
    break

  #Bisection algorithm
  if current_savings - down_payment <= high_epsilon:
    low = percent
    print('Low becomes high')
  else:
    high = percent
    print('High becomes low')
  bisection += 1
  percent = (high + low)//2

  #Infinite loop check
  if low == high:
    print('It is not possible to pay the down payment in three years.')
    break
