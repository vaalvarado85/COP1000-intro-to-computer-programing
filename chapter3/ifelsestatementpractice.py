BASE_HOURS = 40 #base hours for week
OT_MULTIPLIER = 1.5 #overtime multiplier
#Get the number of hours worked
hours_worked = float (input('Enter worked hours:'))
#Get the hourly pay rate
hourly_pay_rate = float(input('Enter hourly pay rate:'))
#calculate and display the gross pay
if hours_worked > BASE_HOURS:
    #calculate the gross pay with overtime
    #first, get the number of overtime hours worked
    overtime_hours = hours_worked-BASE_HOURS

    #calculate the amount of overtime pay
    overtime_pay = overtime_hours * hourly_pay_rate * OT_MULTIPLIER

    #calculate the gross pay
    gross_pay = BASE_HOURS * hourly_pay_rate + overtime_pay
else:
    #calculate the gross pay without overtime
    gross_pay = hours_worked  * hourly_pay_rate

#display the gross pay
print(f'the gross pay is ${gross_pay:,.2f}')