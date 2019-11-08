#Program that calculates the amount of time it will take to save up for a down payment on a house in the bay area

#Annual Salary 
salary = float(input('What is your yearly salary: '))
#Percent of salary to save 
percent_saved = float(input('Percent of salary to save (as a decimal): '))
#Total cost of the home
total_cost = float(input('Total cost of your dream home: '))
#Down payment portion of total cost
down_payment_portion = 0.25
#Current savings 
curr_saving = 0 
month = 0
#Salary per month
sal_per_month = salary/12
#savings 
savings = percent_saved*sal_per_month

#while loop that has logic for adding all the portions together
while curr_saving < total_cost*down_payment_portion:
  curr_saving = curr_saving + savings + curr_saving*.04/12
  month = month + 1

#Print number of months it will take to save up
print('Months: ' + str(month))