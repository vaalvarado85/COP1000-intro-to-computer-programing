#This program calculates the sum of a series of number entered by the user.
#The max number
MAX = 5
#Initialize an accumulator variable
total = 0.0

#Explain what we are doing.
print('This program calculates the sum of', end='')
print(f'{MAX}numbers you will enter.')

#Get the numbers and accumulate them.
for counter in range (MAX):
    number = int(input('Enter a number:'))
    total = total + number

    #Display the total of the numbers.
    print(f'the total is {total}.')