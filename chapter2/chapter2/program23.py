#Victoria Alvarado cop1000 
#prompt user for numerator 
#prompt user for denominator
#calculate integer division 
#canculate remainder
#combine calculated variables
#display mixed number

#get numerator from user
numerator = int(input('Enter numerator:'))
#get denominator from user
denominator = int(input('Enter denominator:'))
#calculate integer value by dividing the numerator by the denominator
calculated_integer = numerator//denominator
#calculated the remainder of the numerator divided by the denominator
calcualted_remainder = numerator%denominator
#display mixed number result
print('The mixed number is ' ,calculated_integer,' and ',calcualted_remainder, '/',denominator,sep='')
