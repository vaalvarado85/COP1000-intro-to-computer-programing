#Victoria Alvarado cop1000 
#prompt user for selling price of the property
#prompt percent commission rate
#convert commision rate
#calculate commision earned
#displayed the commision earned

#get selling price
selling_price =float(input('Enter selling price of the property:'))
#get commission rate
commission_rate = float(input('Enter commission rate:'))
#convert commission rate to decimal 
converted_commision_rate = commission_rate/100
#calculate commission earned 
calculated_commision_earned = selling_price * converted_commision_rate
#displaying commission earned
print(f'The commision earned is ${calculated_commision_earned:,.2f}')