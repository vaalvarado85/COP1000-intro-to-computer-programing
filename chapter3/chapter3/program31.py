#Victoria Alvarado  2317120 COP1000
#Get an integer from user
#Determine and display if the integer is odd or even

#Get integer from user
integer_number = int(input('Enter an integer number'))
#Get remainder 
remainder = integer_number % 2
#if statement to display if a number is even or odd
if remainder== 0:
    print(f"{integer_number} is even.")
else:
     print(f"{integer_number} is odd.")
