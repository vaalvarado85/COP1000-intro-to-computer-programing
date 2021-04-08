#Victoria Alvarado COP1000
#use for loop with range of integers from 5 to 50 in increments of 5
#Get the square number of current number variable
#Get the cube number of current number variable
#Display the table with 3 columns and 7 characters wide

#for loop to iterate the range between 5 to 50 by increment of 5
for number in range (5,51,5):
    #calculate the square of the number variable
    square = number ** 2
    #calculate the cube of the number and square
    cube = square * number
    #Display table with results
    print(f'{number:7}{square:7}{cube:7}')
    