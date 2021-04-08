#Victoria Alvarado COP1000
#prompt the user to enter an integer
#use while loop to check if use is 0 to quit
#if statement to check whether the input was even or odd
#prompt the user to enter another integer

#create a variable to hold the quit integer
end_number = 0
#Get an integer number from the user
integer = int(input('Enter an integer number or 0 to quit: '))
#Use a while loop and an if statement to determinate an even or odd number
while integer != end_number:
    if integer % 2 == 0 :
        print(f'{integer} is a even number!')
    else:
        print(f'{integer} is a odd number!')
#Create a variable to enter another integer from the user
    integer = int(input('Enter an integer number or 0 to quit: '))   
print('All done!!!')