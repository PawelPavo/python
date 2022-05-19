#tuple unpacking as a for loop

stock_prices=[('APPL', 200),('GOOG', 400),('MSFT',150)]

for item in stock_prices:
    print(item)


for ticker, price in stock_prices:
    print(ticker)

for ticker, price in stock_prices:
    print(price+(0.1*price))



#tuple unpacking in a function

work_hours = [('John', 100),('Peter', 700),('Luke', 800)]

#who worked the most hours
def employee_check (work_hours):
    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return(employee_of_month, current_max)

print(employee_check(work_hours))

#this is common to unpack tupls and pass it as separat variables
#common error may be if you have too many vars ex 3, but the function
#only returns 2 ERROR - (not enough values to unpack (expected 3, got 2)
#THIS MEANS THAT YOU EXPECTED 3 but function returns only 2
#to deal with it, assign the whole tuple to a value and see what you get

name,hours = employee_check(work_hours)
print(name)
print(hours)
