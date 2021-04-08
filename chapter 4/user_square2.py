#This program uses a loop to display a table of numbers and their squares
#Get the starting value.
print ('this program displays a list of number')
print ('and their squares')
start = int(input('Enter the starting number:'))

#Get the ending limit
end = int(input('How high should I go?'))

#print the table headings.
print()
print('number/tsquare')
print('----------')

#print the numbers and their squares.
for number in range (star, end + 1):
    square = number ** 2
    print (f'{number}/t{square}')
